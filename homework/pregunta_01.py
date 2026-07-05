"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os
def pregunta_01():
    ruta_salida = "files/output/solicitudes_de_credito.csv"
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    df = pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';')
    # Eliminar filas donde TODAS las columnas son exactamente iguales
    df = df.drop_duplicates(keep='first')
    df['sexo']=df['sexo'].str.lower()
    df['sexo'] = df['sexo'].str.strip()
    df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].astype(str).str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.strip()
    df = df.dropna(subset=['tipo_de_emprendimiento'])
    df = df.dropna(subset=['barrio'])
    df = df.dropna(subset=['sexo'])
    df = df.dropna(subset=['idea_negocio'])
    
    df = df.dropna()

    df['idea_negocio']=df['idea_negocio'].astype(str).str.  lower()
    df['idea_negocio'] = df['idea_negocio'].replace('_',' ')
    df['idea_negocio'] = df['idea_negocio'].str.strip()
    df['comuna_ciudadano']=df['comuna_ciudadano'].astype(str).str.strip()
    df['estrato'] = df['estrato'].astype(str).str.strip()
    df['monto_del_credito'] = df['monto_del_credito'].astype(int)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='%d/%m/%Y', errors='coerce')
    # 1. Asegurar que sea texto, quitar espacios, el signo $ y las comas de miles
    df['monto_del_credito'] = df['monto_del_credito'].astype(str).str.strip().str.replace('$', '').str.replace(',', '')
    df['monto_del_credito'] = df['monto_del_credito'].astype(float).astype(int)
    
    df.to_csv(ruta_salida, index=False, sep=';', encoding='utf-8')



    


    


    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
