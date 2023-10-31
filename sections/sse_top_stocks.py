import datetime
import streamlit as st
from helpers.charts import *
from helpers.processing import *

metric = 'F050201B'
type_rep = 'A'
year = 2015
industries = []
ownership = []
number_displayed = 30

def top_stocks(df):
    filters()
    apply_filters = st.button('Apply Filters', type='primary', key='top_stocks_button')
    if 'sse_top_stocks' not in st.session_state:
        # Create the initial chart and store it in session_state
        st.session_state.sse_top_stocks_title, st.session_state.sse_top_stocks = generate_df(df)

    # Check if the button is clicked
    if apply_filters:
        # Regenerate the chart and update it in session_state
        st.session_state.sse_top_stocks_title, st.session_state.sse_top_stocks = generate_df(df)

    st.markdown(f'''</br><strong style="font-size: 24px;">{st.session_state.sse_top_stocks_title}</strong>''', unsafe_allow_html=True)
    st.table(st.session_state.sse_top_stocks)

def generate_df(df):
    global metric
    global type_rep
    global year
    global industries
    global ownership
    global number_displayed

    if len(industries) == 0: industries = df['Indnme_En'].unique().tolist()
    if len(ownership) == 0: ownership = df['ownership'].unique().tolist()
    if metric in read_metrics_rv()['code'].tolist(): type_rep = None

    title = f'Top {number_displayed} Shanghai stocks ranked by {get_metrics_dict()[metric]} for the year {year}'

    return title, get_top_stocks(
        df,
        number_displayed,
        metric,
        type_rep,
        year,
        industries,
        ownership
    )

def filters():
    global metric
    global type_rep
    global year
    global industries
    global ownership
    global number_displayed

    number_selection, metric_selection, year_selection, industry_selection, ownership_selection = st.columns(5)

    with number_selection.container():
        selected_number = st.selectbox('Select Number of Stocks', options=[x for x in range(10, 501)], key="number_selection_sse", help="Select the number of top stocks you wish to display")
        number_displayed = selected_number

    with metric_selection.container():
        metric_list = get_metrics()

        selected_metric = st.selectbox("Select Metric", options=metric_list['name'], key="metric_selection_sse", help="Search the metric you want to use")
        metric = metric_list.loc[metric_list['name'] == selected_metric, 'code'].values[0]

        if metric in read_metrics()['code'].tolist():
            selected_type_rep = st.selectbox("Select Type Representation", options=['Consolidated Statements', 'Parent Statements'], key="type_rep_sse", help="Selected type representation will be displayed for all applicable and chosen metric")
            type_rep = 'A' if selected_type_rep == 'Consolidated Statements' else 'B'

    with year_selection.container():
        selected_year = st.selectbox('Select Year', options=[x for x in range(datetime.datetime.now().year, datetime.datetime.now().year - 50, -1)], key="year_selection_sse", help=f"All years from {datetime.datetime.now().year - 50} to {datetime.datetime.now().year} are listed even if the stock is not available")
        year = selected_year

    with industry_selection.container():
        industries_list = get_shanghai_data()['Indnme_En'].unique().tolist()
        
        industry = st.multiselect('Select Industry', options=industries_list, key='industry_selection_sse', help='Select industry(s) of choice')
        industries = industry

    with ownership_selection.container():
        ownership_list = get_shanghai_data()['ownership'].unique().tolist()
        
        selected_owership = st.multiselect("Select Ownership Type", options=ownership_list, key="ownership_selection_sse", help=f"Select the ownership type you wish to view")
        ownership = selected_owership

