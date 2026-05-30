
import streamlit as st
import pandas as pd

#data = { "GSE": ["GSE111842","GSE51827"], "Patients": [33,10], "Cancer":["Breast","Breast"]}
#df = pd.DataFrame(data)
df = pd.read_csv("CTC_RNA_Seq-DATA_Search.csv", encoding="latin1")

st.title("CTC RNA-seq Database")



st.sidebar.header("Filtered Datasets")
if "Cancer" in df.columns:
  cancer = st.sidebar.selectbox(
    "Cancer type",
    ["All"] + sorted(df["Cancer"].dropna().unique().tolist())
  )
  if cancer != "All":
    df = df[df["Cancer"] == cancer]

search_term = st.text_input("Search datasets(GEO, Refrence, Cancer, etc.)")

if search_term:
  df = df[df.apply(
    lambda row: row.astype(str).str.contains(search_term, case=False).any(),
    axis=1
  )]

st.dataframe(df)
