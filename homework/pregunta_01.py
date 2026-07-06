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

    df = df.dropna()
    
    df['idea_negocio']=df['idea_negocio'].astype(str).str.lower()
    df['idea_negocio'] = df['idea_negocio'].replace("_", " ", regex=False)
    df['idea_negocio'] = df['idea_negocio'].replace("-", " ", regex=False)
    df['idea_negocio'] = df['idea_negocio'].str.strip()

    df['barrio'] = (
    df['barrio']
    .astype(str)                                  # 0. Asegurar que todo sea texto (evita errores con nulos)
    .str.lower()                                  # 1. Todo a minúsculas
    .str.replace('_', ' ', regex=False)           # 2. Cambia guiones bajos por espacios ("bombona no. 1")
    .str.replace(r'no\.(\d+)', r'no. \1', regex=True) # 3. Separa "no.1" a "no. 1" (le pone espacio si detecta un número pegado)
    .str.replace(r'\s+no\.\s*$', '', regex=True)  # 4. Borra el " no." del final si quedó huérfano (ej. "san jose de la cima no. ")
    .str.replace(r'\s+', ' ', regex=True)         # 5. Convierte cualquier espacio doble o triple en uno solo
    .str.strip()                                  # 6. Elimina espacios en blanco al principio o al final de la frase
    )

    df['comuna_ciudadano']=df['comuna_ciudadano'].astype(str).str.strip()
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)

    df['estrato'] = df['estrato'].astype(str).str.strip()
    df['estrato'] = df['estrato'].astype(int)

    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], errors='coerce')
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime('%Y/%m/%d')
    df = df.dropna(subset=['fecha_de_beneficio'])
    # 1. Asegurar que sea texto, quitar espacios, el signo $ y las comas de miles
    # Limpiar y convertir la columna a entero
    df['monto_del_credito'] = (
        df['monto_del_credito']
        .astype(str)                             # 1. Asegurarnos de que Pandas lo trate como texto
        .str.replace(r'[$, ]', '', regex=True)   # 2. Quitar el $, las comas y los espacios de un solo golpe
        .astype(float)                           # 3. Convertir a decimal primero (vital por el .00)
        .astype(int)                             # 4. Cortar los decimales y dejarlo como entero puro
    )
    
    df.price = df.price.astype(int)
    df['línea_credito'] = df['línea_credito'].astype(str).str.lower().str.strip()

    df.to_csv(ruta_salida, index=False, sep=';', encoding='utf-8')



    


    


    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
