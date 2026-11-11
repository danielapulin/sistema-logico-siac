"""
Módulo de Base de Datos (base_datos.py)
-----------------------------------------------------------------------------
Este archivo centraliza el manejo de la persistencia de datos. Utiliza el 
módulo nativo 'json' de Python para guardar los registros de los postulantes 
en un archivo local, simulando una base de datos segura y estructurada.
"""

import json
import os

# Nombre del archivo donde se guardarán los datos de forma permanente
DB_FILE = "candidatos_db.json"

def cargar_base_datos():
    """
    Lee el archivo JSON con los registros de los candidatos.
    Si el archivo no existe o está vacío, retorna una lista vacía para 
    evitar que el programa falle (manejo básico de excepciones).
    """
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as archivo:
            try:
                # Intentamos cargar el contenido como una lista de diccionarios
                return json.load(archivo)
            except json.JSONDecodeError:
                # Si el archivo se corrompió o está vacío, devolvemos lista vacía
                return []
    return []

def guardar_candidato(nuevo_registro):
    """
    Recibe un diccionario con los datos del postulante evaluado,
    lo agrega a la lista existente y lo vuelve a guardar en el archivo JSON.
    """
    # 1. Traemos los datos que ya estaban guardados
    datos_actuales = cargar_base_datos()
    
    # 2. Añadimos el nuevo registro al final de la lista
    datos_actuales.append(nuevo_registro)
    
    # 3. Sobrescribimos el archivo con la lista actualizada y formato legible (indent=4)
    with open(DB_FILE, "w", encoding="utf-8") as archivo:
        json.dump(datos_actuales, archivo, indent=4, ensure_ascii=False)