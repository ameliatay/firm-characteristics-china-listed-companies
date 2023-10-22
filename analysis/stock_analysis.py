import streamlit as st
import pandas as pd
from analysis.data_enum import DATASTORE

def process_csv():
  roa_a_data = pd.read_csv("datasets/roa/stocks_ROA_A_avg.csv", names=["ticker", "year", "roa"], header=0)
  st.session_state[DATASTORE.ROA_A_DF] = roa_a_data
  st.session_state[DATASTORE.ROA_A_TICKERS] = roa_a_data['ticker'].unique()

  roa_b_data = pd.read_csv("datasets/roa/stocks_ROA_B_avg.csv", names=["ticker", "year", "roa"], header=0)
  st.session_state[DATASTORE.ROA_B_DF] = roa_b_data
  st.session_state[DATASTORE.ROA_B_TICKERS] = roa_b_data['ticker'].unique()

  roa_c_data = pd.read_csv("datasets/roa/stocks_ROA_C_avg.csv", names=["ticker", "year", "roa"], header=0)
  st.session_state[DATASTORE.ROA_C_DF] = roa_c_data
  st.session_state[DATASTORE.ROA_C_TICKERS] = roa_c_data['ticker'].unique()

  st.session_state[DATASTORE.SHENZHEN_DF] = st.session_state[DATASTORE.ROA_A_DF]
  st.session_state[DATASTORE.SHENZHEN_ALL_TICKERS] = st.session_state[DATASTORE.ROA_A_TICKERS]
  st.session_state[DATASTORE.SHENZHEN_SELECTED_TICKERS] = []

  st.session_state[DATASTORE.SHANGHAI_DF] = st.session_state[DATASTORE.ROA_A_DF]
  st.session_state[DATASTORE.SHANGHAI_ALL_TICKERS] = st.session_state[DATASTORE.ROA_A_TICKERS]
  st.session_state[DATASTORE.SHANGHAI_SELECTED_TICKERS] = []
  
  st.session_state['data_processed'] = True

def plot_shenzhen_chart():
  tickers = st.session_state[DATASTORE.SHENZHEN_SELECTED_TICKERS] if len(st.session_state[DATASTORE.SHENZHEN_SELECTED_TICKERS]) > 0 else st.session_state[DATASTORE.SHENZHEN_ALL_TICKERS]
  start_year = st.session_state[DATASTORE.SHENZHEN_START]
  end_year = st.session_state[DATASTORE.SHENZHEN_END]
  df = st.session_state[DATASTORE.SHENZHEN_DF]

  result_df = df[(df['ticker'].isin(tickers)) & (df['year'] >= start_year) & (df['year'] <= end_year)]
  st.line_chart(result_df.reset_index(inplace=False), x="year", y="roa", color="ticker")

def plot_shanghai_chart():
  tickers = st.session_state[DATASTORE.SHANGHAI_SELECTED_TICKERS] if len(st.session_state[DATASTORE.SHANGHAI_SELECTED_TICKERS]) > 0 else st.session_state[DATASTORE.SHANGHAI_ALL_TICKERS]
  start_year = st.session_state[DATASTORE.SHANGHAI_START]
  end_year = st.session_state[DATASTORE.SHANGHAI_END]
  df = st.session_state[DATASTORE.SHANGHAI_DF]

  result_df = df[(df['ticker'].isin(tickers)) & (df['year'] >= start_year) & (df['year'] <= end_year)]
  st.line_chart(result_df.reset_index(inplace=False), x="year", y="roa", color="ticker")