# Stock exchange analytics dashboard built on Streamlit
_View it live on https://firm-characteristics-of-china-listed-companies.streamlit.app/_

<img width="1792" alt="Screenshot 2023-10-31 at 5 36 41 PM" src="https://github.com/ameliatay/firm-characteristics-china-listed-companies/assets/83273830/0e0d682c-a87b-4b10-b5c5-8459b8255636">
<img width="1792" alt="Screenshot 2023-10-31 at 5 36 59 PM" src="https://github.com/ameliatay/firm-characteristics-china-listed-companies/assets/83273830/95e93152-4a2c-43d9-bb6f-87da5759b133">
<img width="1792" alt="Screenshot 2023-10-31 at 5 37 11 PM" src="https://github.com/ameliatay/firm-characteristics-china-listed-companies/assets/83273830/77265b42-b754-4655-bc21-faabec56c921">

## Features
Specifically focused on analysing firm characteristics of stocks on the Shenzhen and Shanghai exchanges. Some features users can look forward to are
- Get a quick indication of the top n number of stocks for a chosen metric
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
