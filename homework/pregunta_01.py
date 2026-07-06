"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import os
import pandas as pd

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    input_path = "files/input/solicitudes_de_credito.csv"
    output_dir = "files/output"
    output_path = os.path.join(output_dir, "solicitudes_de_credito.csv")

    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(input_path, sep=";", index_col=0)

    df.dropna(inplace=True)

    df["sexo"] = df["sexo"].str.lower().str.strip()

    df["tipo_de_emprendimiento"] = (
        df["tipo_de_emprendimiento"].str.lower().str.strip()
    )

    df["idea_negocio"] = (
        df["idea_negocio"]
        .str.lower()
        .str.replace("_", " ")
        .str.replace("-", " ")
        .str.strip()
    )

    df["barrio"] = (
        df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    )

    df["estrato"] = df["estrato"].astype(int)

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(float)

    def parse_date(date_str):
        if "/" in date_str:
            parts = date_str.split("/")
            if len(parts[0]) == 4:
                return f"{parts[2]}/{parts[1]}/{parts[0]}"
            else:
                return f"{parts[0].zfill(2)}/{parts[1].zfill(2)}/{parts[2]}"
        return date_str

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(parse_date)
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%d/%m/%Y"
    )

    df["monto_del_credito"] = (
        df["monto_del_credito"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df["monto_del_credito"] = (
        df["monto_del_credito"].str.split(".").str[0].astype(float)
    )

    df["línea_credito"] = (
        df["línea_credito"]
        .str.lower()
        .str.replace("_", " ")
        .str.replace("-", " ")
        .str.strip()
    )

    df.drop_duplicates(inplace=True)

    df.to_csv(output_path, sep=";", index=False)

    return