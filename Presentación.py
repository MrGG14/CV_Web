import streamlit as st

# Configurar el ancho de la página
# st.set_page_config(layout="wide")


# # Añadir el fondo de pantalla usando CSS

# page_element = """
# <style>
# [data-testid="stAppViewContainer"] {
#   background-image: url("https://digitalpm.es/wp-content/uploads/2017/11/3881153-big-data-wallpaper.jpg");
#   background-size: cover;
#   background-attachment: fixed;
# }
# .content-box {
#   background-color: rgba(255, 255, 255, 0.8);
#   padding: 20px;
#   border-radius: 10px;
#   box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#   margin: 20px;
# }
# </style>
# """

# st.markdown(page_element, unsafe_allow_html=True)
# st.markdown('<div class="content-box">', unsafe_allow_html=True)

# Encabezado con foto de perfil
st.title('Nicolás Vega Muñoz')
st.write("## **Data Scientist**")
st.image('img.jpeg', width=170)

# Información de contacto

st.write("**nicovegamunoz1@gmail.com**")
st.write('**(+34) 654 27 29 28**')
st.write('**Madrid, España**')
st.write('[**GitHub**](https://github.com/MrGG14)')
st.write('[**LinkedIn**](https://www.linkedin.com/in/nicolas-vega-10424021b/)')


# Sobre Mi
st.write("## ¿Quién soy?")
st.write('Actualmente soy estudiante de 4º curso en el grado de Ciencia de Datos e Inteligencia Artificial. Mi pasion por la informatica , y en concreto por la inteligencia artificial se ha ido reforzando durante estos años en los que he sido formado en la Universidad Politecnica de Madrid. He adquirido amplios conocimientos en el ambito de la estadistica, aprendizaje automatico, deep learning, analisis de datos y cloud entre otros. Tras haber tenido mi primera experiencia en el mercado laboral me gustaria poder aportar mis conocimientos al sector al que quiero dedicarme, el automovilismo.')
st.write('Me considero una persona responsable, social, organizada y sobre todo con muchas ganas de aprender en esta primera etapa laboral de mi vida.')
st.write("""
    Estoy motivado y listo para aplicar mis conocimientos en un entorno empresarial que me permita crecer profesionalmente.
""")
# Oferta de Empleo
st.write("\n")
st.write("## Oferta de empleo Hyundai")

st.write("### Data Analyst en Hyundai Motor España, S.L.U.")
st.write("**Ubicación:** Madrid y alrededores")
st.write("**Modalidad:** Híbrido")
st.write("**Jornada:** Completa")
st.write("**Experiencia:** Intermedio")
st.write("**Empleados:** De 51 a 200 empleados")
st.write("**Descripción:**")
st.write("""
- **Misión:** Liderar junto con el resto del equipo de Transformación Digital el proyecto de centralización del dato, migración entre herramientas de visualización hacia Power BI y cumplir con las necesidades de los usuarios.
- **Funciones:**
  - Diseñar modelos de datos intuitivos para el usuario.
  - Coordinar la creación del modelo con los responsables del lago de datos.
  - Creación y gestión de cuadros de mando necesarios y solicitados por negocio, para la gestión en la toma de decisiones.
  - Soporte en la coordinación entre los equipos de gobierno del dato, desarrollo e infraestructura del proyecto de Business Intelligence.
  - Gestión de la documentación necesaria para la gestión de los modelos, datos y cuadros de mando (métricas, objetivos, etc.).
  - Liderar la transformación de los datos, su análisis y participar en el gobierno del dato como asesor.
- **Conocimientos:**
  - Experiencia en la toma de requisitos y en el diseño funcional en soluciones de analítica descriptiva.
  - Experiencia en diseño de métricas y visualizaciones adecuadas para abordarlas.
  - Capacidad de entendimiento de negocio.
  - Capacidad de extracción de conclusiones y análisis con sentido de estrategia de negocio y propuesta de mejora.
  - Perfil analítico muy marcado.
  - Proactividad y liderazgo.
  - Gestión de proyectos.
- **Perfil:**
  - Experiencia de al menos 3 años trabajando con Power BI en puesto similar.
  - Nivel avanzado SQL, DAX y lenguaje M (valorable).
  - Conocimiento de extracción y transformación de datos en Power Query (valorable).
  - Imprescindible experiencia en proyectos de Power BI en entorno Power BI Service (Azure).
  - Valorables conocimientos de Microsoft Fabric.
  - Metodología Agile.
  - Inglés B2 hablado y escrito.
- **¿Qué ofrecemos?:**
  - Participación en un proyecto innovador de gran aportación de valor empresarial y con impacto en el negocio, donde encontrarás un entorno dinámico en el cual hay espacio para nuevas ideas y mejoras.
  - Trabajarás con el equipo de implementación del DataLake e inteligencia de negocio en colaboración con consultores expertos.
  - El puesto es el nexo entre el área funcional y el área de desarrollo.
  - Trabajarás con tecnologías emergentes en el entorno de Microsoft Azure Cloud.
  - Modalidad de trabajo híbrida y horario flexible.
- **Compromiso con la Diversidad:** Hyundai está firmemente comprometida con la diversidad e igualdad de oportunidades y garantiza que en todos sus procesos de selección no habrá discriminación por razones de raza, nacionalidad, género, orientación o identidad sexual, edad, estado civil, creencias religiosas o discapacidad.
""")
st.link_button("Ver oferta en LinkedIn", "https://www.linkedin.com/jobs/view/data-analyst-at-hyundai-motor-espa%C3%B1a-s-l-u-3919648191/?originalSubdomain=es")

# Carta de Presentacion
st.write("\n")
st.write("**Carta de Presentación Analista Datos Hyundai:**")
with open("carta_motivacion.pdf", "rb") as pdf_file:
    carta_presentacion = pdf_file.read()
st.download_button("Descargar Carta de Presentacion", data=carta_presentacion, file_name='Carta de Presentacion.pdf', mime='application/pdf')

