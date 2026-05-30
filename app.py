
import streamlit as st
import pandas as pd

#data = { "GSE": ["GSE111842","GSE51827"], "Patients": [33,10], "Cancer":["Breast","Breast"]}
#df = pd.DataFrame(data)
df = pd.read_csv("CTC_RNA_Seq-DATA_Search.csv", encoding="latin1")


st.sidebar.header("Filtered Datasets")
if "Cancer" in df.columns:
  cancer = st.sidebar.selectbox(
    "Cancer type",
    ["All"] + sorted(df["Cancer"].dropna().unique().tolist())
  )
  if cancer != "All":
    df = df[df["Cancer"] == cancer]

st.subheader("Search Datasets")
geo_search = st.text_input("Search by GEO accession(e.g., GSE112856)")

if geo_search and "GEO" in df.columns:
  df = df[df["GEO"].astype(str).str.contains(geo_search, case=False, na=False)]

keyword_search = st.text_input("Keyword search(summery or refrence)")

if keyword_search:
  text_cols = [c for c in ["summery", "refrence"] if c in df.columns]
  if text_cols:
    df = df[df[text_cols].astype(str).apply(
      lambda row: row.str.contains(keyword_search, case=False, na=False).any(),
      axis=1
    )]

if "patients CTCS" in df.columns:
  patient_only = st.checkbox("Show patient-derived CTC datasets only")
  if patient_only:
    df = df[df["patient CTCs"].astype(str).str.contains("yes", case=False, na=False)]
st.dataframe(df)
