import datetime
import streamlit as st

from helpers.processing import *
from helpers.charts import *

companies = []
metric_one = 'F050201B'
metric_two = 'No selection'
type_rep = 'A'
year = 2015
industries = []
ownership = []
result_df = []

def scatterplot(df):
    global result_df
    global metric_one
    global metric_two
    result_df = df

    filters()
    replot_chart = st.button('Replot Chart', type='primary', key='scatter_button')

    col1, col2 = st.columns([0.9, 0.1])
    with col1.container():
        # Check if the chart has been created
        if 'sse_scatter' not in st.session_state:
            # Create the initial chart and store it in session_state
            st.session_state.sse_scatter = generate_chart(df)
            st.session_state.sse_scatter_stats = [result_df, metric_one, metric_two]

        # Check if the button is clicked
        if replot_chart:
            # Regenerate the chart and update it in session_state
            st.session_state.sse_scatter = generate_chart(df)
            st.session_state.szse_scatter_stats = [result_df, metric_one, metric_two]

        # Display the chart from session_state
        st.plotly_chart(st.session_state.sse_scatter, use_container_width=True)

    with col2.container(): statistics()

def generate_chart(df):
    global companies
    global metric_one
    global metric_two
    global type_rep
    global year
    global industries
    global ownership
    global result_df

    if len(industries) == 0: industries = df['Indnme_En'].unique().tolist()
    if len(companies) == 0: companies = df['final_company_name'].unique().tolist()
    if len(ownership) == 0: ownership = df['ownership'].unique().tolist()
    if metric_one in read_metrics_rv()['code'].tolist() and metric_two in read_metrics_rv()['code'].tolist(): type_rep = None

    if metric_two == 'No selection':
        fig, df = scatterplot_one_metric(
            df, 
            'Shanghai',
            year, 
            companies, 
            metric_one, 
            type_rep, 
            industries,
            ownership
        )
    else:
        print('im here')
        fig, df = scatterplot_two_metrics(
            df, 
            'Shanghai',
            year, 
            metric_one, 
            metric_two, 
            type_rep, 
            companies, 
            industries,
            ownership
        )
    result_df = df
    return fig    
    

def filters():
    global companies
    global metric_one
    global metric_two
    global type_rep
    global year
    global industries
    global ownership

    companies, metrics, year_filter, industry, ownership_selected = st.columns([1,2,1,1,1])

    with companies.container():
        tickers = get_shanghai_tickers()
        
        selected_stock = st.multiselect("Select Tickers", options=tickers, key="ticker", help="Search or type the ticker you want to view")
        companies = selected_stock

    with metrics.container():
        metric1, metric2 = st.columns(2)

        with metric1.container():
            metric_1_list = get_metrics()
            
            selected_metric_1 = st.selectbox("Select Metric One", options=metric_1_list['name'], key="metric_1", help="Search the metric you want to use")
            metric_one = metric_1_list.loc[metric_1_list['name'] == selected_metric_1, 'code'].values[0]

        with metric2.container():
            metrics_2 = get_metrics()['name'].tolist()
            metrics_2.insert(0, 'No selection')
            metrics_2.remove(selected_metric_1)

            selected_metric_2 = st.selectbox("Select Metric Two (Optional)", options=metrics_2, key="metric_2", help="Search the metric you want to use",)
            if selected_metric_2 != 'No selection':
                metric_two = metric_1_list.loc[metric_1_list['name'] == selected_metric_2, 'code'].values[0]
            else: metric_two = 'No selection'

        if metric_one in read_metrics()['code'].tolist() or metric_two in read_metrics()['code'].tolist():
            selected_type_rep = st.selectbox("Select Type Representation", options=['Consolidated Statements', 'Parent Statements'], key="type_rep_one", help="Selected type representation will be displayed for all applicable and chosen metrics")
            type_rep = 'A' if selected_type_rep == 'Consolidated Statements' else 'B'

    with year_filter.container():
        periods = [x for x in range(datetime.datetime.now().year, datetime.datetime.now().year - 50, -1)]
        
        selected_year = st.selectbox("Select Year", options=periods, key="year_shanghai", help=f"All years from {datetime.datetime.now().year - 50} to {datetime.datetime.now().year} are listed even if the stock is not available")
        year = selected_year

    with industry.container():
        industries_list = get_shanghai_data()['Indnme_En'].unique().tolist()
        
        industry = st.multiselect('Select Industry', options=industries_list, key='industry', help='Select industry(s) of choice')
        industries = industry

    with ownership_selected.container():
        ownership_list = get_shanghai_data()['ownership'].unique().tolist()
        
        selected_owership = st.multiselect("Select Ownership Type", options=ownership_list, key="ownership_shanghai", help=f"Select the ownership type you wish to view")
        ownership = selected_owership

def statistics():
    result_df, metric_one, metric_two = st.session_state.sse_scatter_stats

    st.metric('Number of Tickers', len(result_df))

    metric_one_en = get_metrics().loc[get_metrics()['code'] == metric_one, 'name'].values[0]
    st.metric(f'Average {metric_one_en}', round(result_df[metric_one].mean(),4))
    st.metric(f'Minimum {metric_one_en}', round(result_df[metric_one].min(),4))
    st.metric(f'Maximum {metric_one_en}', round(result_df[metric_one].max(),4))

    if metric_two != 'No selection':
        metric_two_en = get_metrics().loc[get_metrics()['code'] == metric_two, 'name'].values[0]
        st.metric(f'Average {metric_two_en}', round(result_df[metric_two].mean(),4))
        st.metric(f'Minimum {metric_two_en}', round(result_df[metric_two].min(),4))
        st.metric(f'Maximum {metric_two_en}', round(result_df[metric_two].max(),4))