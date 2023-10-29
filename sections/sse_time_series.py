import datetime
import streamlit as st

from helpers.processing import *
from helpers.charts import *

companies = []
metric = 'F050201B'
type_rep = 'A'
start_year = 2000
end_year = 2023
industries = []

def time_series(df):
    filters()
    replot_chart = st.button('Replot Chart', type='primary', key='time_button')

    if 'sse_time' not in st.session_state:
        st.session_state.sse_time = generate_charts(df)

    if replot_chart:
        st.session_state.sse_time = generate_charts(df)

    col1, col2, col3 = st.columns(3)
    with col1.container():
        st.plotly_chart(st.session_state.sse_time[0], use_container_width=True)
        st.plotly_chart(st.session_state.sse_time[3], use_container_width=True)
        st.plotly_chart(st.session_state.sse_time[6], use_container_width=True)

    with col2.container():
        st.plotly_chart(st.session_state.sse_time[1], use_container_width=True)
        st.plotly_chart(st.session_state.sse_time[4], use_container_width=True)
        st.plotly_chart(st.session_state.sse_time[7], use_container_width=True)

    with col3.container():
        st.plotly_chart(st.session_state.sse_time[2], use_container_width=True)
        st.plotly_chart(st.session_state.sse_time[5], use_container_width=True)
        st.plotly_chart(st.session_state.sse_time[8], use_container_width=True)

def generate_charts(df):
    global companies
    global metric
    global type_rep
    global start_year
    global end_year
    global industries

    if len(industries) == 0: industries = df['Indnme_En'].unique().tolist()
    if len(companies) == 0: companies = df[df['Indnme_En'].isin(industries)]['final_company_name'].unique().tolist()[:10]

    return [
        # 1
        plot_time_series(
            df,
            'Shanghai',
            start_year, 
            end_year, 
            companies, 
            'F050201B', 
            type_rep, 
            industries
        ),
        # 2
        plot_time_series(
            df,
            'Shanghai',
            start_year, 
            end_year, 
            companies, 
            'F051501B', 
            type_rep, 
            industries
        ),
        # 3
        plot_time_series(
            df,
            'Shanghai',
            start_year, 
            end_year, 
            companies, 
            'F050501B', 
            type_rep, 
            industries
        ),
        # 4
        plot_time_series(
            df,
            'Shanghai',
            start_year, 
            end_year, 
            companies, 
            'F011701A', 
            type_rep, 
            industries
        ),
        # 5
        plot_time_series(
            df,
            'Shanghai',
            start_year, 
            end_year, 
            companies, 
            'F010201A', 
            type_rep, 
            industries
        ),
        # 6
        plot_time_series(
            df,
            'Shanghai',
            start_year, 
            end_year, 
            companies, 
            'F010101A', 
            type_rep, 
            industries
        ),
        # 7
        plot_time_series(
            df,
            'Shanghai',
            start_year, 
            end_year, 
            companies, 
            'F090101B', 
            type_rep, 
            industries
        ),
        # 8
        plot_time_series(
            df,
            'Shanghai',
            start_year, 
            end_year, 
            companies, 
            'F100401A', 
            None, 
            industries
        ),
        # 9
        plot_time_series(
            df,
            'Shanghai',
            start_year, 
            end_year, 
            companies, 
            'F100101B', 
            None, 
            industries
        ),
    ]

def filters():
    global companies
    global metric
    global type_rep
    global start_year
    global end_year
    global industries

    ticker_selection, type_rep_selection, start_year_selection, end_year_selection, industry = st.columns(5)

    with ticker_selection.container():
        tickers = get_shanghai_tickers()
        
        selected_stock = st.multiselect("Select Tickers", options=tickers, key="ticker_time", help="If no ticker is selected, the first 10 tickers will be returned", max_selections=10)

        companies = selected_stock

    with type_rep_selection.container():
        type_rep_selected = st.selectbox("Select Type Representation", options=['A', 'B'], key="type_rep", help="Search the type representation you want to use")

        type_rep = type_rep_selected

    with start_year_selection.container():
        periods = [x for x in range(datetime.datetime.now().year, datetime.datetime.now().year - 50, -1)]
        
        year = st.selectbox("Select Start Year", options=periods, key="start_sse", index=49, help=f"All years from {datetime.datetime.now().year - 50} to {datetime.datetime.now().year} are listed")

        start_year = year

    with end_year_selection.container():
        periods = [x for x in range(datetime.datetime.now().year, start_year, -1)]
        
        year = st.selectbox("Select End Year", options=periods, key="end_sse", help=f"All years from {datetime.datetime.now().year - 50} to {datetime.datetime.now().year} are listed")

        end_year = year

    with industry.container():
        industries_list = get_shanghai_data()['Indnme_En'].unique().tolist()
        
        industry = st.multiselect('Select Industry', options=industries_list, key='industry_time', help='Select industry(s) of choice')

        industries = industry