import streamlit as st
from sections.szse_scatter import *
from sections.szse_time_series import *
from sections.szse_top_stocks import *

def shenzhen():
    df = get_shenzhen_data()

    st.write('''Officially founded in 1990&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of listings: 2,375 as of January 2021&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Website: <a href="https://www.szse.cn/English/index.html">szse.cn<a/>''', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Compare top stocks", "Compare against market averages", "Compare against other stocks"])

    with tab1: top_stocks(df)
    with tab2: scatterplot(df)
    with tab3: time_series(df)
