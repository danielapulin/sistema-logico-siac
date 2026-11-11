"""
Módulo de Propuesta y Modelo (propuesta.py)
-----------------------------------------------------------------------------
Define la formalización del problema, cumpliendo con la Etapa 1 de la rúbrica.
Aquí establecemos las variables proposicionales que alimentarán nuestro motor lógico.
"""

# Metadatos formales del proyecto exigidos por la cátedra
PROYECTO_INFO = {
    "titulo": "SIEC - Sistema Inteligente de Evaluación de Candidatos",
    "linea_tematica": "Línea 02: Motor de validación de inscripciones y perfiles",
    "descripcion_problema": (
        "Sistema automatizado de selección de talento que evalúa criterios "
        "lógicos, técnicos, actitudinales y documentales mediante álgebra booleana."
    ),
    "dominio_aplicacion": "Gestión de Recursos Humanos y Admisiones Académicas"
}

# Diccionario de variables lógicas (Dominio booleano {0, 1})
# Desde la mirada de RRHH, estas son las 4 dimensiones clave de aptitud y idoneidad.
VARIABLES_LOGICAS = {
    "L": {
        "nombre": "Prueba de Lógica Formal",
        "descripcion": "Evalúa razonamiento deductivo y resolución de silogismos.",
        "peso_logico": "Variable proposicional L"
    },
    "T": {
        "nombre": "Capacidad Técnica",
        "descripcion": "Evalúa conocimientos fundamentales de programación y algoritmos.",
        "peso_logico": "Variable proposicional T"
    },
    "S": {
        "nombre": "Habilidades Sociales",
        "descripcion": "Evalúa inteligencia emocional, trabajo en equipo y empatía.",
        "peso_logico": "Variable proposicional S"
    },
    "E": {
        "nombre": "Requisito Documental Excluyente",
        "descripcion": "Verifica si el candidato cumple con antecedentes y disponibilidad legal.",
        "peso_logico": "Variable proposicional E"
    }
}

def mostrar_propuesta():
    """Función para imprimir de forma clara la propuesta en la consola."""
    print("=" * 70)
    print(f" PROYECTO: {PROYECTO_INFO['titulo']}")
    print("=" * 70)
    print(f"• Línea Temática: {PROYECTO_INFO['linea_tematica']}")
    print(f"• Objetivo: {PROYECTO_INFO['descripcion_problema']}\n")
    print("--- DICCIONARIO DE VARIABLES BOOLEANAS ---")
    for var, info in VARIABLES_LOGICAS.items():
        print(f"[{var}] {info['nombre']}: {info['descripcion']}")
    print("=" * 70)