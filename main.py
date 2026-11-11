"""
=============================================================================
TRABAJO FINAL INTEGRADOR - LÓGICA COMPUTACIONAL
INSTITUCIÓN: IES 9-008 Manuel Belgrano
CARRERA: Tecnicatura Superior en Desarrollo de Software
ESTUDIANTE: Daniela Jacqueline Pulin
PROYECTO: SIEC (Sistema Inteligente de Evaluación de Candidatos)
=============================================================================

PUNTO DE ENTRADA PRINCIPAL (main.py)
"""

from propuesta import mostrar_propuesta
from modelo_matematico import mostrar_modelo_matematico
from evaluacion import ejecutar_evaluacion
from test_validador import ejecutar_pruebas_sistema
from admin import mostrar_panel_admin

def main():
    """Bucle principal del sistema con el menú de opciones."""
    while True:
        print("\n" + "="*55)
        print("   SISTEMA INTELIGENTE DE EVALUACIÓN (SIEC) - MENÚ")
        print("="*55)
        print("1. Ver Propuesta y Variables (Etapa 1)")
        print("2. Ver Modelo Matemático y Tabla de Verdad (Etapa 2)")
        print("3. Realizar Test de Postulación (Candidato)")
        print("4. Ejecutar Pruebas Automatizadas del Sistema (Etapa 4)")
        print("5. Panel de Administración (RRHH - Datos Sensibles)")
        print("6. Salir del Sistema")
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        if opcion == "1":
            mostrar_propuesta()
        elif opcion == "2":
            mostrar_modelo_matematico()
        elif opcion == "3":
            ejecutar_evaluacion()
        elif opcion == "4":
            ejecutar_pruebas_sistema()
        elif opcion == "5":
            mostrar_panel_admin()
        elif opcion == "6":
            print("\nSaling del sistema SIEC. ¡Hasta luego, Daniela!")
            break
        else:
            print("\n[!] Opción inválida. Por favor, ingrese un número del 1 al 6.")

if __name__ == "__main__":
    main()
    
    #python main.py