"""
Módulo de Administración (admin.py)
-----------------------------------------------------------------------------
Gestiona el acceso restringido a los datos sensibles de los postulantes
mediante un control de contraseña.
"""

from base_datos import cargar_base_datos

# Contraseña segura para el panel de administración
PASSWORD_ADMIN = "Admin9008#"

def mostrar_panel_admin():
    """Verifica credenciales y despliega la tabla con los resultados de los candidatos."""
    print("\n" + "="*60)
    print("   PANEL DE ADMINISTRACIÓN DE RECURSOS HUMANOS (DATOS SENSIBLES)")
    print("="*60)
    
    # Control de acceso por seguridad (datos sensibles)
    password = input("Ingrese la contraseña de administrador: ").strip()
    
    if password != PASSWORD_ADMIN:
        print("\n[X] ACCESO DENEGADO: Contraseña incorrecta.")
        return

    print("\n[✔] ACCESO CONCEDIDO. Cargando registros de postulantes...")
    datos = cargar_base_datos()
    
    if not datos:
        print("\n[i] No hay postulantes registrados en el sistema todavía.")
        return

    print(f"\nTotal de candidatos evaluados: {len(datos)}")
    print("-" * 75)
    print(f"{'N°':<3} | {'Nombre y Apellido':<22} | {'DNI':<10} | {'Variables (L,T,S,E)':<18} | {'Resultado'}")
    print("-" * 75)
    
    for idx, c in enumerate(datos, start=1):
        v = c["variables"]
        resumen_vars = f"L:{v['L']} T:{v['T']} S:{v['S']} E:{v['E']}"
        print(f"{idx:<3} | {c['nombre']:<22} | {c['dni']:<10} | {resumen_vars:<18} | {c['resultado']}")
    
    print("-" * 75)