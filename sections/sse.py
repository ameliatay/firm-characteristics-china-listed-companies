import streamlit as st
from sections.sse_scatter import *
from sections.sse_time_series import *
from sections.sse_top_stocks import *

def shanghai():
    df = get_shanghai_data()

    st.write('''Officially founded in 1990&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of listings: 2,005 as of July 2021&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Website: <a href="http://english.sse.com.cn/">english.sse.com.cn<a/>''', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Compare top stocks", "Compare against market averages", "Compare against other stocks"])

    with tab1: top_stocks(df)
    with tab2: scatterplot(df)
    with tab3: time_series(df)
