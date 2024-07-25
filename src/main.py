import ssl
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

from datetime import datetime
from repository.data_repository import load_data_gsheet
from repository.indicators_services import calculate_payments
from pages.incomes import incomes

# Setup SSL certificate to run requests
ssl._create_default_https_context = ssl._create_unverified_context
# Page Layout
st.set_page_config(page_title='Edificio Manhattan',  layout="wide",
                   page_icon='../assets/skyscraper-with-antennas.png',
                   initial_sidebar_state="collapsed"
                   )

df = load_data_gsheet()

df_with_statistics = calculate_payments(df)

incomes_tab, outcomes_tab = st.tabs(["Receitas", "Despesas"])

with incomes_tab:
    incomes(df_with_statistics)

with outcomes_tab:
    st.title('Despesas')
