import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
from services.chart_builder import chartBuilder


def incomes(df: pd.DataFrame):

    with st.container():

        st.title('Dashboard de Receitas do Condominio')

        df = df[df['Mês de Pagamento'].dt.year <= datetime.now(
        ).year]

        selected_status = st.multiselect(
            'Selecione o status do pagamento', df['Status'].unique(), placeholder="Selecione a situação de pagamento")

        st.divider()

        if selected_status != []:
            df_filtered = df[df['Status'].isin(
                selected_status)]

            st.dataframe(df_filtered, use_container_width=True,
                         selection_mode='multiple')

        else:
            st.dataframe(df, use_container_width=True)

        st.divider()

        col1, col2, col3 = st.columns(3)

        col1.plotly_chart(chartBuilder(
            'line', df), use_container_width=True)
        col2.plotly_chart(chartBuilder('bar', df),
                          use_container_width=True)
        col3.plotly_chart(chartBuilder('pie', df),
                          use_container_width=True)
