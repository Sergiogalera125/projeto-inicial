
import streamlit as st
import pandas as pd


# Reads Excel with a single time series
# no dates column, top row with series name



st.set_page_config(page_title="vai timao",
                   layout="wide")
st.title('Testando planilha excell')

st.sidebar.title('World Happiness Index 2021:')

st.image('Pedro_Fernanda_Wurlitzer.jpg')

st.image('Tomas_Fernanda_Wurlitzer.jpg')

#excel_data_df = pd.read_excel('teste planilha.xlsx', sheet_name='Planilha1', usecols=['a', 'b','c','d','e','f'])
#print(excel_data_df)

