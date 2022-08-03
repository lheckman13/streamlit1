import pandas as pd
import streamlit as st
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
#read csv
  df1=pd.read_csv(uploaded_file)
  #df1=df1.sample(frac=1)
  col1=df1[0:5]
  col2=df1[5:10]
  col3=df1[10:15]
  final=pd.DataFrame()
  final['B']=col1
  final['I']=col2
  final['N']=col3
  with st.container():
  st.dataframe(final, width=500, height=500)
