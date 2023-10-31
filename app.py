import streamlit as st
from pathlib import Path
import base64
from streamlit_option_menu import option_menu
from sections.szse import shenzhen
from sections.sse import shanghai
from sections.key_definitions import key_definitions

# Initial page config

if 'selected' not in st.session_state:
    st.session_state['selected'] = "Shenzhen Exchange"


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
            width: 380px !important; 
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
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' height=80>](https://github.com/ameliatay)'''.format(img_to_bytes("assets/china-flag.png")), unsafe_allow_html=True)
    st.sidebar.header('Firm characteristics of china-listed companies')

    with st.sidebar:
        st.session_state['selected'] = option_menu(None, ['Shenzhen Exchange', 'Shanghai Exchange', 'Key Definitions'], 
            icons=['bar-chart-line-fill', 'bar-chart-line-fill', 'key-fill'], menu_icon="cast")
        
    st.sidebar.markdown('''<br><br><br><br>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<small>This dashboard was created as part of Singapore Management University's Capital Markets in China (AY2023-2024 Semester 1) course to aid interested parties better analyse China-listed stocks on the Shenzhen and Shanghai exchange in a more user-intuitive manner.</small>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<br>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<small style="font-weight: bold;">Professor Wang Jiwei</small><br><small style="font-weight: bold;">Section G1 Team 5</small><br><small>[Chen Jian Yu](https://www.linkedin.com/in/chen-jian-yu/) | [Parmesh Harvadan Mehta](https://www.linkedin.com/in/parmesh-mehta/) | [Natalie Chua](https://www.linkedin.com/in/nataliechua2000/) | [Amelia Tay](https://www.linkedin.com/in/amelia-tay-li-jia) | [Lee Ling Hui](https://www.linkedin.com/in/leelinghui/) | [Isaac Tan](https://www.linkedin.com/in/isaac-tan-e-9605171ab/)</small>''', unsafe_allow_html=True)

    return None

# Main body of cheat sheet

def cs_body():
    st.title(st.session_state['selected'])
    if st.session_state['selected'] == "Shanghai Exchange": shanghai()
    elif st.session_state['selected'] == "Key Definitions": key_definitions()
    else: shenzhen()

    return None

if __name__ == '__main__':
    main()
