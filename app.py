
import streamlit as st
import pandas as pd

data = { "GSE: ["GSE111842","GSE51827"], "Patients": [33,10], "Cancer":["Breast",Breast"]}
df = pd.DataFrame(data)

st.title("CTC RNA-seq Database")

st.dataframe(df)
