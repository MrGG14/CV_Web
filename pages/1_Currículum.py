import streamlit as st


# Configurar el ancho de la página
# st.set_page_config(layout="wide")
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #6A0083;
    }
</style>
""", unsafe_allow_html=True)
# Encabezado con foto de perfil
st.write("# Nicolás Vega Muñoz")
st.write("## **Data Scientist**")
st.image('img.jpeg', width=170)

# Información de contacto

# Información de contacto
st.write("📧 [**Correo**](mailto:nicovegamunoz1@gmail.com)")
st.write("📱 **(+34) 654 27 29 28**")
st.write("🔗 [**GitHub**](https://github.com/MrGG14)")
st.write("🔗 [**LinkedIn**](https://www.linkedin.com/in/nicolas-vega-10424021b/)")
st.write("📍 **Madrid, España**")


# Experiencia Laboral
st.write("## Experiencia Laboral")
st.write("- **NTT Data (Mayo 2024 - Presente)**: *Data Scientist Junior en Estrategia Digital/Analítica Avanzada*")
st.write("""
    - Colaboración en la automatización y pre-industrialización del proyecto 'Forecast of Electric Market Price'.
""")

# Proyectos
st.write("## Proyectos")
st.write("- **Forecast del precio SPOT en el mercado eléctrico español con redes neuronales (Trabajo de Fin de Grado)**")
st.write("""
    Predicción de series temporales utilizando machine learning (CNN, LSTM) y modelos de vanguardia como Temporal Fusion Transformers (TFT).
""")
st.link_button("¡Ver en Github!", "https://github.com/MrGG14/Electricity-Price-Forecast-NN")


st.write("- **SureBets Strategy Automatization**")
st.write("""
    Adquisición de datos desde The Odds API y scraping de casas de apuestas. Automatización de apuestas matemáticamente garantizadas en diversas plataformas de apuestas. Desarrollo de un TelegramBot que obtiene surebets.
""")
st.link_button("¡Ver en Github!", "https://github.com/MrGG14/SureBet-Strategy-Automatization")


st.write("- **Superstore Membership Conversion Predictor**")
st.write("""
    Predicción de la probabilidad de que el cliente acepte una nueva oferta de un supermercado, reduciendo costos de marketing y aumentando la tasa de conversión.
""")
st.link_button("¡Ver en Github!", "https://github.com/MrGG14/Superstore_Membership_Conversion_Predictor")


st.write("- **Content Based Image Retrieval (CBIR)**")
st.write("""
    Implementación de múltiples sistemas de recuperación de imágenes basados en contenido utilizando descriptores locales y globales de imágenes, como texturas, puntos de interés (SIFT) y Redes Neuronales Convolucionales (CNN).
""")
st.link_button("¡Ver en Github!", "https://github.com/MrGG14/CBIR")


# Formación
st.write("## Formación")
st.write("- **Universidad Politécnica de Madrid (2020 - 2024)**: *Grado en Ciencia de Datos e Inteligencia Artificial*")
st.write("- **IES Burgo de Las Rozas (2020)**: *Excelencia Académica en Bachillerato Tecnológico*")

# Habilidades
st.write("## Habilidades")
st.write("**Lenguajes de Programación:** Python, R, SQL")
st.write("**Machine Learning:** Deep Learning, CNN, LSTM, Gradient Boosting, Adaboost, Bagging, Grid Search, (S)ARIMA")
st.write("**Big Data:** MapReduce, Hadoop, Apache Kafka")
st.write("**Ciencia de Datos y Procesamiento de Datos:** NLP, Semantic Web, Web Scraping, Estadísticas, MapReduce, CRISP-DM")
st.write("**Herramientas:** Anaconda, Github, Docker")
st.write("**Nube:** Amazon AWS")
st.write("**Bases de Datos:** MySQL, SQLite, Neo4j, MongoDB")
st.write("**Librerías:** TensorFlow, Keras, Scikit-learn, PyTorch, NumPy, Pandas, OpenCV, Selenium, BeautifulSoup, Matplotlib")
st.write("**Otros:** IoT, Criptografía, MatLab")
st.write("**Soft Skills :** Resolución de Problemas, Trabajo en Equipo, Búsqueda y Análisis de Información, Liderazgo, Creatividad, Organización")

# Idiomas
st.write("## Idiomas")
st.write("**Inglés:** C1 (Cambridge)")
st.write("**Español:** Nativo")

# Descargar CV
st.write("## Conóceme más:")
with open("CV_NVM_may24.pdf", "rb") as pdf_file:
    cv_tradicional = pdf_file.read()

with open("CV Infografico.pdf", "rb") as pdf_file:
    cv_infografico = pdf_file.read()

st.download_button("Descargar CV Tradicional", data=cv_tradicional, file_name= 'CV_NVM_may24.pdf', mime='pdf')
st.download_button("Descargar CV Infográfico", data=cv_infografico, file_name= 'CV Infografico.pdf', mime='pdf')
st.link_button("Vídeo Currículum", "https://youtu.be/MmxAe4zzdQ8")