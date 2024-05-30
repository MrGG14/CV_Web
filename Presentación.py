import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Configurar el ancho de la página
st.set_page_config(layout="wide")
# Agregar estilos personalizados para el sidebar
# Add a selectbox to the sidebar:
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #6A0083;
    }
</style>
""", unsafe_allow_html=True)

def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = 'Nicolás Vega Muñoz'
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Bienvenido! Soy {full_name}👋", 'Data Scientist')
    st.write("")
    # st.write(info['About'])



# Sobre Mi
st.write("## ¿Quién soy?")
st.write('Actualmente soy estudiante de 4º curso en el grado de Ciencia de Datos e Inteligencia Artificial. Mi pasion por la informatica , y en concreto por la inteligencia artificial se ha ido reforzando durante estos años en los que he sido formado en la Universidad Politecnica de Madrid. He adquirido amplios conocimientos en el ambito de la estadistica, aprendizaje automatico, deep learning, analisis de datos y cloud entre otros. Tras haber tenido mi primera experiencia en el mercado laboral me gustaria poder aportar mis conocimientos al sector al que quiero dedicarme, el automovilismo.')
st.write('Me considero una persona responsable, social, organizada y sobre todo con muchas ganas de aprender en esta primera etapa laboral de mi vida.')
st.write("""
    Estoy motivado y listo para aplicar mis conocimientos en un entorno empresarial que me permita crecer profesionalmente.
""")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# loading assets
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")


with st.container():
    st.subheader('⚒️ Herramientas')
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(docker_lottie,height=70,width=70, key="docker", speed=2.5)

    with col3:
        st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=70,width=70, key="git", speed=2.5)
    with col5:
        st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)

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

