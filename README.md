# Stock exchange analytics dashboard built on Streamlit
_View it live on https://firm-characteristics-of-china-listed-companies.streamlit.app/_

<img width="1920" alt="Screenshot 2023-10-30 at 10 09 07 AM" src="https://github.com/ameliatay/firm-characteristics-china-listed-companies/assets/83273830/99f96693-6d42-4f9c-986e-c9a5217b6064">

<img width="1920" alt="Screenshot 2023-10-30 at 10 08 47 AM" src="https://github.com/ameliatay/firm-characteristics-china-listed-companies/assets/83273830/58e57f27-904e-4b17-87ca-5d7d2e352c31">

## Features
Specifically focused on analysing firm characteristics of stocks on the Shenzhen and Shanghai exchanges. Some features users can look forward to are
- Comparing stock performance in a particular year against market averages (Or averages of the selected stocks, picked using the drop-down menu)
- Compare stock performance over time across 9 different metrices
- Filters for stock name / code / company name, ownership type, period, industry, metric, and metric representation

## Set up (One time)
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip3 install streamlit`
- `pip3 install plotly`
- `pip3 install pandas`
- `pip3 install streamlit_option_menu`

## Running the app locally
- `streamlit run app.py`
