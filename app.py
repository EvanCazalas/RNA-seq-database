
import streamlit as st
import pandas as pd

#data = { "GSE": ["GSE111842","GSE51827"], "Patients": [33,10], "Cancer":["Breast","Breast"]}
#df = pd.DataFrame(data)
df = pd.read_csv("CTC_RNA_Seq-DATA_Search.csv", encoding="latin1")

st.title("CTC RNA-seq Database")

st.dataframe(df)

