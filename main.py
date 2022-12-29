

import pandas as pd
# import plotly.express as px
import streamlit as st

# Reads Excel with a single time series
# no dates column, top row with series name

st.set_page_config(page_title="vai timao",
                   layout="wide")
st.title('Testando planilha excell')

st.sidebar.title('Zé Burguelas')

st.image('Pedro_Fernanda_Wurlitzer.jpg')

st.image('Tomas_Fernanda_Wurlitzer.jpg')

df = pd.read_excel(
    io='planilha.xlsx',
    engine='openpyxl',
    sheet_name='carro',
    skiprows=1,
    usecols='A:F',
    nrows=500,
)

# print(df)

st.write(df)