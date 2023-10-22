import datetime
import streamlit as st
from analysis.data_enum import DATASTORE
from analysis.stock_analysis import plot_shenzhen_chart

def shenzhen_stocks():
    filter_stock()

    col1, col2 = st.columns([0.7, 0.3])
    with col1.container():
        plot_shenzhen_chart()
    with col2.container():
        st.subheader("This is for statistics")

def filter_stock():
    ticker_selection, measure_selection, start_year_selection, end_year_selection = st.columns(4)

    with ticker_selection.container():
        selected_stock = st.multiselect("Select Tickers", options=st.session_state[DATASTORE.SHENZHEN_ALL_TICKERS], key="ticker_shenzhen", help="Search or type the ticker you want to view", default=st.session_state[DATASTORE.SHENZHEN_SELECTED_TICKERS])
        st.session_state[DATASTORE.SHENZHEN_SELECTED_TICKERS] = selected_stock

    with measure_selection.container():
        measures = ['ROA A', 'ROA B', 'ROA C']
        selected_measure = st.selectbox("Select Measure", options=measures, key="measure_shenzhen")
        
        if selected_measure == "ROA A":
            st.session_state[DATASTORE.SHENZHEN_DF] = st.session_state[DATASTORE.ROA_A_DF]
        elif selected_measure == "ROA B":
            st.session_state[DATASTORE.SHENZHEN_DF] = st.session_state[DATASTORE.ROA_B_DF]
        elif selected_measure == "ROA C":
            st.session_state[DATASTORE.SHENZHEN_DF] = st.session_state[DATASTORE.ROA_C_DF]

    with start_year_selection.container():
        periods = [x for x in range(datetime.datetime.now().year, datetime.datetime.now().year - 50, -1)]
        selected_period = st.selectbox("Select Start Period", options=periods, index=49, key="start_shenzhen", help=f"All years from {datetime.datetime.now().year - 50} to {datetime.datetime.now().year} are listed even if the stock is not available")
        st.session_state[DATASTORE.SHENZHEN_START] = selected_period  

    with end_year_selection.container():
        periods = [x for x in range(datetime.datetime.now().year, datetime.datetime.now().year - 50, -1)]
        selected_period = st.selectbox("Select End Period", options=periods, key="end_shenzhen", help=f"All years from {datetime.datetime.now().year - 50} to {datetime.datetime.now().year} are listed even if the stock is not available")
        st.session_state[DATASTORE.SHENZHEN_END] = selected_period  


