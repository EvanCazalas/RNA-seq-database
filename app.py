
import streamlit as st
import pandas as pd

#data = { "GSE": ["GSE111842","GSE51827"], "Patients": [33,10], "Cancer":["Breast","Breast"]}
#df = pd.DataFrame(data)
df = pd.read_csv("CTC_RNA_Seq-DATA_Search.csv", encoding="latin1")

st.title("CTC RNA-seq Database")

st.dataframe(df)

st.sidebar.header("Filtered Datasets")
if "Cancer" in df.columns:
  cancer = st.sidebar.selectbox(
    "Cancer type",
    ["All"] + sorted(df["Cancer"].dropna().unique().tolist())
  )
  if cancer != "All":
    df = df[df["Cancer"] == cancer]

st.dataframe(df)
