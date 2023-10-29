import streamlit as st

from helpers.processing import get_metrics

def key_definitions():
    st.table(get_metrics())