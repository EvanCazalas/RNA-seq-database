
import streamlit as st
import pandas as pd

df = pd.read_csv("CTC_RNA_Seq-DATA_Search.csv", encoding="latin1")


st.sidebar.header("Filtered Datasets")
if "Cancer" in df.columns:
  cancer = st.sidebar.selectbox(
    "Cancer type",
    ["All"] + sorted(df["Cancer"].dropna().unique().tolist())
  )
  if cancer != "All":
    df = df[df["Cancer"] == cancer]


st.subheader("Search datasets")


geo_search = st.text_input("Search by GEO accession (e.g., GSE112856)")

if geo_search and "GEO" in df.columns:
    df = df[df["GEO"].astype(str).str.contains(geo_search, case=False, na=False)]

keyword_search = st.text_input("Keyword search (summary or reference)")

if keyword_search:
    text_cols = []
    if "summery" in df.columns:
        text_cols.append("summery")
    if "refrence" in df.columns:
        text_cols.append("refrence")

    if text_cols:
        df = df[df[text_cols].astype(str).apply(
            lambda row: row.str.contains(keyword_search, case=False, na=False).any(),
            axis=1
        )]

if "patient CTCS" in df.columns:
    patient_only = st.checkbox("Show patient-derived CTC datasets only")
    if patient_only:
        df = df[df["patient CTCS"].astype(str).str.contains("yes", case=False, na=False)]

st.dataframe(df)
