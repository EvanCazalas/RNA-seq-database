
import streamlit as st
import pandas as pd


df = pd.read_csv(
    "CTC_RNA_Seq-DATA_Search(True_File).csv",
    encoding="latin1",
    sep=",",
    dtype=str,
    keep_default_na=False
)

st.write("✅ File loaded")
st.write("Shape:", df.shape)
st.write("Columns:")
st.write(list(df.columns))

st.write("First 10 rows (raw):")
st.write(df.head(10))


df.columns = df.columns.str.strip()

st.title("CTC RNA-seq Database")

st.subheader("Search datasets")

geo_search = st.text_input("Search by GEO accession (e.g., GSE112856)")

if geo_search and "GEO" in df.columns:
    df = df[df["GEO"].astype(str).str.contains(geo_search, case=False, na=False)]
    

st.write("Preview of summary column:")
if "summery" in df.columns:
    st.write(df["summery"].head(10))

st.write("Preview of reference column:")
if "refrence" in df.columns:
    st.write(df["refrence"].head(10))


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
