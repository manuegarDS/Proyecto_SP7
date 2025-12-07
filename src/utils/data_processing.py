import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    # Convertir columnas a tipo correcto

    df["model_year"] = df["model_year"].astype("Int64")
    df["cylinders"] = df["cylinders"].astype("Int64")
    df["odometer"] = df["odometer"].astype("Int64")
    df["is_4wd"] = df["is_4wd"].astype("Int64")
    df["date_posted"] = pd.to_datetime(df["date_posted"])

    # Eliminar filas duplicadas

    df = df.drop_duplicates()

    # Convertir nombres de columnas a snake_case

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    return df
