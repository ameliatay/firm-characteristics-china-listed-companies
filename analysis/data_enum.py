from enum import Enum


class DATASTORE(Enum):
  SHENZHEN_DF = 'shenzhen_df'
  SHENZHEN_SELECTED_TICKERS = 'shenzhen_selected_tickers'
  SHENZHEN_ALL_TICKERS = 'shenzhen_all_tickers'
  SHENZHEN_START = 'shenzhen_start'
  SHENZHEN_END = 'shenzhen_end'

  SHANGHAI_DF = 'shanghai_df'
  SHANGHAI_SELECTED_TICKERS = 'shanghai_selected_tickers'
  SHANGHAI_ALL_TICKERS = 'shanghai_all_tickers'
  SHANGHAI_START = 'shanghai_start'
  SHANGHAI_END = 'shanghai_end'

  ROA_A_DF = 'roa_a_data'
  ROA_A_TICKERS = 'roa_a_tickers'
  ROA_B_DF = 'roa_b_data'
  ROA_B_TICKERS = 'roa_b_tickers'
  ROA_C_DF = 'roa_c_data'
  ROA_C_TICKERS = 'roa_c_tickers'