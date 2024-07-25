import streamlit as st
import pandas as pd


def load_data_gsheet():
    gsheet_id = '11jIDWITyBuluJNEvPxbKlDbTUyqbnSH9ByLad2zd3Ss'
    gsheet_name = 'payments'
    gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(
        gsheet_id, gsheet_name)
    df = pd.read_csv(gsheet_url)

    cleaned_df = df.loc[:, ~df.columns.str.startswith('Unnamed:')]

    return cleaned_df
