import pandas as pd

def format_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    for index, row in df.iterrows():
        df.at[index, "Valor do Condominio"] = f"R$ {
            row['Valor do Condominio']:.2f}"
    return df
