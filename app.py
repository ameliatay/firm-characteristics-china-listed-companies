import datetime
import streamlit as st
from pathlib import Path
import base64
from analysis.stock_analysis import process_csv
from sections.key_insights import key_insights
from sections.shanghai_overview import shanghai_overview
from sections.shanghai_stocks import shanghai_stocks
from sections.shenzhen_stocks import shenzhen_stocks
from sections.shenzhen_overview import shenzhen_overview
from streamlit_option_menu import option_menu

# Initial page config

if 'selected' not in st.session_state:
    st.session_state['selected'] = "Key Insight"

if 'data_processed' not in st.session_state or not st.session_state['data_processed']:
    st.session_state['data_processed'] = False
    process_csv()


st.set_page_config(
     page_title='CMC G2T5 Dashboard',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()

    return None

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 360px !important; 
        }
        .main .block-container {
            padding-top: 30px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# sidebar

def cs_sidebar():
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' height=80>](https://streamlit.io/)'''.format(img_to_bytes("assets/china-flag.png")), unsafe_allow_html=True)
    st.sidebar.header('Firm characteristics of china-listed companies')

    with st.sidebar:
        st.session_state['selected'] = option_menu(None, ["Key Insights", '---', 'Shenzhen Exchange Overview', 'Shenzhen Stocks', '---', 'Shanghai Exchange Overview', 'Shanghai Stocks', '---'], 
            icons=['key-fill', None, 'bar-chart-line-fill', 'building-fill-up', None, 'bar-chart-line-fill', 'building-fill-up'], menu_icon="cast")
        
    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<small>Chen Jian Yu | Parmesh Harvadan Mehta | Natalie Chua | Amelia Tay | Lee Ling Hui | Isaac Tan</small>''', unsafe_allow_html=True)

    return None

# Main body of cheat sheet

def cs_body():
    st.title(st.session_state['selected'])
    if st.session_state['selected'] == "Shenzhen Exchange Overview": shenzhen_overview()
    elif st.session_state['selected'] == "Shanghai Exchange Overview": shanghai_overview()
    elif st.session_state['selected'] == "Shenzhen Stocks": shenzhen_stocks()
    elif st.session_state['selected'] == "Shanghai Stocks": shanghai_stocks()
    else: key_insights()
    return None

if __name__ == '__main__':
    main()
