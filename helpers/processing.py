import streamlit as st
import pandas as pd

@st.cache_data
def read_metrics():
  return pd.read_csv("datasets/metrics.csv")

@st.cache_data
def read_metrics_rv():
  return pd.read_csv("datasets/metrics_rv.csv")

@st.cache_data
def get_metrics():
  df1 = read_metrics()
  df2 = read_metrics_rv()
  return pd.concat([df1, df2])

@st.cache_data
def get_shenzhen_data():
  raw_df = pd.read_csv("datasets/shenzhen.csv")
  return raw_df

@st.cache_data
def get_shenzhen_tickers():
  return get_shenzhen_data()['final_company_name'].unique()

@st.cache_data
def get_shanghai_data():
  raw_df = pd.read_csv("datasets/shanghai.csv")
  return raw_df

@st.cache_data
def get_shanghai_tickers():
  return get_shanghai_data()['final_company_name'].unique()