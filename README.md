# SIEC (Sistema Inteligente de Evaluación de Candidatos)

Proyecto Final Integrador para la asignatura **Lógica Computacional**  
**Institución:** IES 9-008 Manuel Belgrano  
**Carrera:** Tecnicatura Superior en Desarrollo de Software  
**Estudiante:** Daniela Jacqueline Pulin  

---

##  Descripción del Proyecto
El **SIEC** es un sistema inteligente desarrollado en Python que automatiza el proceso de preselección de postulantes (para puestos laborales o becas tecnológicas) aplicando un motor de decisiones basado en lógica proposicional, álgebra de boole y funciones simplificadas mediante mapas de Karnaugh.

El sistema evalúa cuatro dimensiones clave del candidato:
1. **L (Lógica):** Resolución de pruebas de razonamiento deductivo y silogismos.
2. **T (Técnica):** Fundamentos de programación y algoritmos.
3. **S (Sociales):** Competencias actitudinales, empatía y resolución de conflictos.
4. **E (Excluyente):** Verificación de cumplimiento documental y normativo.

---

##  Arquitectura y Estructura del Código
El proyecto está desarrollado bajo un enfoque modular para separar responsabilidades y facilitar su mantenimiento y exposición:

```text
siec_proyecto/
│
├── main.py             #  Punto de entrada principal (Menú general)
├── propuesta.py        #  Etapa 1: Formalización teórica y variables lógicas
├── evaluacion.py       #  Motor del test interactivo y evaluación booleana
├── admin.py            #  Panel de recursos humanos protegido por contraseña
├── base_datos.py       #  Módulo de persistencia local (lectura/escritura JSON)
├── candidatos_db.json  #  Base de datos generada automáticamente
└── README.md           #  Documentación técnica del proyecto
