import pandas as pd
import plotly.express as px
import streamlit as st


def chartBuilder(chart_type, data: pd.DataFrame):
    if chart_type == 'line':
        chart_render = px.line(data, x='Mês de Pagamento', y=[
            'Orcamento Planejado', 'Orcamento Atingido'],
            hover_data=['Percentual Pagamentos'],
            title='Orçamento Planejado x Orçamento Atingido',
            line_dash='variable',
            symbol='variable',
            labels={'value': 'Valor (R$)', 'variable': 'Tipo de Orçamento',
                    'Mês de Pagamento': 'Mês de Pagamento'},
            markers=True,
            color_discrete_map={'Orcamento Planejado': '#3b82f6', 'Orcamento Atingido': '#e5e5e5'})

        return chart_render

    elif chart_type == 'bar':
        chart_render = px.bar(data, x='Mês de Pagamento',
                              y='Percentual Pagamentos',
                              title='Percentual de Pagamentos',
                              labels={'Percentual Pagamentos': 'Percentual (%)',
                                      'Mês de Pagamento': 'Mês de Pagamento'},
                              color='Percentual Pagamentos',
                              color_continuous_scale=px.colors.sequential.Blues)

        return chart_render

    elif chart_type == 'pie':
        chart_render = px.pie(
            data, values=data.groupby('Status')['Status'].count().values,
            names=data['Status'].unique(),
            title='Distribuição de Pagamentos por Status',
            labels={'value': 'Quantidade', 'names': 'Status'}, color_discrete_map=px.colors.qualitative.Prism)

        return chart_render
