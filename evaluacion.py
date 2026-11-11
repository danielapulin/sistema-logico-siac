"""
Módulo de Evaluación y Test (evaluacion.py)
-----------------------------------------------------------------------------
Contiene la lógica interactiva del test para el postulante y aplica el 
motor booleano derivado de la simplificación por mapas de Karnaugh.
"""

from base_datos import guardar_candidato

def evaluar_motor_logico(L, T, S, E):
    """
    Motor lógico basado en la función booleana simplificada:
    F = (T and S and E) or (L and T and S) or (L and T and E)
    
    Donde:
    L = Lógica formal
    T = Capacidad técnica
    S = Habilidades sociales
    E = Requisito documental excluyente
    """
    resultado = (T and S and E) or (L and T and S) or (L and T and E)
    return resultado

def ejecutar_evaluacion():
    """Función principal que guía al postulante a través de las 4 dimensiones."""
    print("\n" + "="*60)
    print("   SISTEMA DE EVALUACIÓN DE POSTULANTES - SIEC")
    print("="*60)
    print("Bienvenido/a. Este proceso evaluará competencias clave para el puesto.")
    
    # 1. Datos personales básicos
    nombre = input("\nIngrese su Nombre y Apellido: ").strip()
    dni = input("Ingrese su DNI: ").strip()
    
    if not nombre or not dni:
        print("[!] Error: Los datos personales son obligatorios para registrar su postulación.")
        return

    print(f"\nMuchas gracias, {nombre}. Comencemos con las evaluaciones.")
    print("-" * 60)

    # --- SECCIÓN 1: LÓGICA FORMAL (Dimensión L) ---
    print("\n[SECCIÓN 1/4] PRUEBA DE RAZONAMIENTO LÓGICO")
    print("Pregunta: Si 'Ningún reptil tiene plumas' y 'Algunas aves tienen plumas',")
    print("¿Se puede deducir lógicamente que 'Algunas aves no son reptiles'?")
    print("  1. Sí, es una conclusión lógicamente válida.")
    print("  2. No, la conclusión es falsa o no se desprende.")
    
    resp_l = input("Elija su opción (1 o 2): ").strip()
    L = 1 if resp_l == "1" else 0

    # --- SECCIÓN 2: CAPACIDAD TÉCNICA (Dimensión T) ---
    print("\n[SECCIÓN 2/4] PRUEBA DE CAPACIDAD TÉCNICA")
    print("Pregunta: En programación básica, ¿cuál es el resultado de evaluar: not(True or False) and True?")
    print("  1. True")
    print("  2. False")
    
    resp_t = input("Elija su opción (1 o 2): ").strip()
    # La respuesta correcta es False (2), por lo tanto T = 1 si elige 2.
    T = 1 if resp_t == "2" else 0

    # --- SECCIÓN 3: HABILIDADES SOCIALES Y SITUACIONALES (Dimensión S) ---
    print("\n[SECCIÓN 3/4] HABILIDADES SOCIALES Y TRABAJO EN EQUIPO")
    print("Pregunta: Ante un conflicto técnico urgente con un compañero de proyecto, ¿cuál es su enfoque?")
    print("  1. Priorizo la comunicación abierta, la empatía y la búsqueda de consenso.")
    print("  2. Trabajo de forma completamente aislada sin discutir el problema con el equipo.")
    
    resp_s = input("Elija su opción (1 o 2): ").strip()
    S = 1 if resp_s == "1" else 0

    # --- SECCIÓN 4: REQUISITO DOCUMENTAL / EXCLUYENTE (Dimensión E) ---
    print("\n[SECCIÓN 4/4] REQUISITO DOCUMENTAL")
    print("¿Cuenta con la disponibilidad horaria requerida y la documentación en regla?")
    print("  1. Sí, cuento con todo en regla.")
    print("  2. No cumplo actualmente con los requisitos documentales.")
    
    resp_e = input("Elija su opción (1 o 2): ").strip()
    E = 1 if resp_e == "1" else 0

    # --- EVALUACIÓN DEL MOTOR LÓGICO ---
    aprobado = evaluar_motor_logico(L, T, S, E)
    estado_str = "APROBADO (Preseleccionado)" if aprobado else "EN REVISIÓN / NO APTO"

    # Empaquetamos los datos para guardarlos de forma estructurada
    nuevo_candidato = {
        "nombre": nombre,
        "dni": dni,
        "variables": {
            "L": L,
            "T": T,
            "S": S,
            "E": E
        },
        "resultado": estado_str
    }

    # Guardamos en la "base de datos" (archivo JSON)
    guardar_candidato(nuevo_candidato)

    # Mensaje de despedida y aviso transparente 
    print("\n" + "="*60)
    print(f" ¡Muchas gracias por su tiempo y participación, {nombre}!")
    print("="*60)
    print("Su test ha sido procesado y registrado exitosamente en el sistema.")
    print("Le informamos que el equipo de Recursos Humanos se pondrá en contacto")
    print("con usted próximamente, **ya sea por sí o por no**, una vez finalizada")
    print("la auditoría técnica de todas las postulaciones.")
    print("="*60)