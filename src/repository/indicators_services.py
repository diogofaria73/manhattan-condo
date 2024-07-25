import pandas as pd


def calculate_payments(df: pd.DataFrame):
    df['Total Mensal'] = df['Valor do Condominio'] + \
        df['Valor do Fundo de Reserva']

    # Identify current status based on registered payments
    df['Status'] = df['Pagamentos Registrados'].apply(
        lambda x: 'Total' if x == 40 else 'Parcial')

    df['Orcamento Planejado'] = df['Total Mensal'] * 40
    df['Orcamento Atingido'] = df['Pagamentos Registrados'] * df['Total Mensal']
    df['Percentual Pagamentos'] = df['Orcamento Atingido'] / \
        df['Orcamento Planejado'] * 100

    df['Mês de Pagamento'] = pd.to_datetime(df['Mês de Pagamento'])

    return df
