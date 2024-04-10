import streamlit as st
import pandas as pd
from pandas import DataFrame
from math import sqrt


import time
import requests
import json

st.title('Danh sach diem danh ngay 4/3/2022')
st.subheader('an')

def run_status():
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Percent Complete {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)
        st.empty()


df = pd.read_excel('test.xlsx')
st.table(df)

