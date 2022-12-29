import xlrd as x1
import matplotlib.pyplot as plt
import xlsxwriter
import numpy
import math
import statistics
import streamlit as st



# Reads Excel with a single time series
# no dates column, top row with series name

st.set_page_config(page_title="vai timao",
                   layout="wide")

st.dataframe("oi")