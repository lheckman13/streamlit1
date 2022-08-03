import pandas as pd
import streamlit as st
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
#read csv
  df1=pd.read_csv(uploaded_file)
  df1=df1.sample(frac=1)
  col1=df1[1:5]
  col2=df1[6:10]
  col3=df1[11:15]
  final=pd.dataframe()
  final['B']=col1
  final['I']=col2
  final['N']=col3
  st.dataframe(final, width=50, height=50)
