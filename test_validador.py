"""
Módulo de Validación y Pruebas (test_validador.py)
-----------------------------------------------------------------------------
Cumple con la Etapa 4 de la rúbrica: ejecuta pruebas automáticas sobre los 
escenarios normales, excepciones y casos límite del sistema.
"""

from evaluacion import evaluar_motor_logico

def ejecutar_pruebas_sistema():
    """Ejecuta una batería de 10 pruebas automatizadas sobre el motor lógico."""
    print("\n" + "="*75)
    print("   ETAPA 4: VALIDACIÓN Y PRUEBAS AUTOMATIZADAS DEL SISTEMA")
    print("="*75)
    print(f"{'Escenario':<10} | {'Descripción de la Prueba':<35} | {'Entradas (L,T,S,E)':<18} | {'Estado'}")
    print("-" * 75)

    # Definición de 10 escenarios exigidos por la cátedra
    escenarios = [
        ("Prueba 01", "Candidato ideal (todo óptimo)", (1, 1, 1, 1), 1),
        ("Prueba 02", "Falla lógica, resto óptimo", (0, 1, 1, 1), 1),
        ("Prueba 03", "Falla técnica (bloqueante)", (1, 0, 1, 1), 0),
        ("Prueba 04", "Falta requisito documental", (1, 1, 1, 0), 1),
        ("Prueba 05", "Sin habilidades sociales", (1, 1, 0, 1), 1),
        ("Prueba 06", "Solo aprueba lógica", (1, 0, 0, 0), 0),
        ("Prueba 07", "Sin lógica ni técnica", (0, 0, 1, 1), 0),
        ("Prueba 08", "Perfil totalmente deficiente", (0, 0, 0, 0), 0),
        ("Prueba 09", "Caso límite: sin lógica ni sociales", (0, 1, 0, 1), 0),
        ("Prueba 10", "Caso límite: sin documental", (1, 1, 1, 0), 1),
    ]

    exitosas = 0
    for esc, desc, entradas, esperado in escenarios:
        l, t, s, e = entradas
        # Obtenemos el resultado booleano del motor (convertido a 1 o 0)
        obt_bool = evaluar_motor_logico(l, t, s, e)
        obtenido = 1 if obt_bool else 0
        
        # Verificamos si coincide el resultado esperado con el obtenido
        if obtenido == esperado:
            estado_str = "✔ CORRECTO"
            exitosas += 1
        else:
            estado_str = "❌ ERROR"

        entradas_str = f"L:{l} T:{t} S:{s} E:{e}"
        print(f"{esc:<10} | {desc:<35} | {entradas_str:<18} | {estado_str}")

    print("-" * 75)
    print(f"Resultado de validación: {exitosas} de {len(escenarios)} pruebas superadas con éxito.")
    print("="*75)