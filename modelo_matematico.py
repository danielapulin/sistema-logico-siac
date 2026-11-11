"""
Módulo de Modelo Matemático (modelo_matematico.py)
-----------------------------------------------------------------------------
Cumple con la Etapa 2 del trabajo final: formalización proposicional, 
funciones booleanas, formas canónicas y simplificación por Karnaugh.
"""

# Resumen formal del modelo para documentar en código y consola
INFO_MATEMATICA = {
    "variables": "L (Lógica), T (Técnica), S (Sociales), E (Documental)",
    "funcion_original": "F(L,T,S,E) = T·S·E + L·T·S + L·T·E",
    "forma_canonica_sop": "F = Σ m(7, 13, 14, 15)",
    "forma_canonica_pos": "F = Π M(0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12)",
    "funcion_simplificada": "F_simplificada = T·S·E + L·T·S + L·T·E"
}

def mostrar_modelo_matematico():
    """Imprime en consola el resumen del modelo matemático y la tabla de verdad."""
    print("\n" + "="*70)
    print("   ETAPA 2: MODELADO LÓGICO Y MATEMÁTICO - SIEC")
    print("="*70)
    print(f"• Variables de Entrada: {INFO_MATEMATICA['variables']}")
    print(f"• Función Booleana: {INFO_MATEMATICA['funcion_original']}")
    print(f"• Forma Canónica SOP: {INFO_MATEMATICA['forma_canonica_sop']}")
    print(f"• Forma Canónica POS: {INFO_MATEMATICA['forma_canonica_pos']}")
    print(f"• Expresión Simplificada (Karnaugh): {INFO_MATEMATICA['funcion_simplificada']}\n")
    
    print("--- TABLA DE VERDAD DEL SISTEMA ---")
    print(f"{'Fila':<5} | {'L':<3} {'T':<3} {'S':<3} {'E':<3} | {'Resultado F(L,T,S,E)'}")
    print("-" * 45)
    
    # Generamos la tabla de verdad programáticamente con las 16 combinaciones
    for l in [0, 1]:
        for t in [0, 1]:
            for s in [0, 1]:
                for e in [0, 1]:
                    # Aplicamos la función lógica simplificada
                    resultado = (t and s and e) or (l and t and s) or (l and t and e)
                    res_num = 1 if resultado else 0
                    fila_id = (l << 3) | (t << 2) | (s << 1) | e
                    print(f"{fila_id:<5} | {l:<3} {t:<3} {s:<3} {e:<3} | {res_num}")
    print("="*70)