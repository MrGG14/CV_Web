import streamlit as st

st.title("Forecasting de Series Temporales para Dummies")




st.subheader("Introducción")
st.write("""
    El forecasting de series temporales es una técnica crucial en el análisis de datos que se utiliza para predecir futuros valores basándose en datos históricos.
    Este método es ampliamente aplicado en diversas industrias, desde la previsión de ventas en el comercio minorista hasta la predicción de la demanda energética.
    En este blog, exploraremos los conceptos fundamentales, métodos populares y aplicaciones prácticas del forecasting de series temporales de una forma entendible para todos!
""")

st.subheader("¿Qué es una Serie Temporal?")
st.write("""
    Una serie temporal es una secuencia de datos puntos ordenados en el tiempo. Estos puntos pueden representar cualquier medida que varíe con el tiempo,
    como la temperatura diaria, las ventas mensuales de una tienda, o los precios de las acciones. La característica principal de las series temporales
    es su dependencia temporal: cada valor depende, en cierto grado, de los valores anteriores.
""")

st.subheader("Componentes de una Serie Temporal")
st.write("""
    Para entender mejor las series temporales, es útil descomponerlas en varios componentes:
    - **Tendencia:** Refleja el cambio a largo plazo en los datos. Por ejemplo, una tendencia creciente en las ventas de una tienda.
    - **Estacionalidad:** Representa patrones repetitivos a a lo largo del tiempo, como las ventas de juguetes aumentando en diciembre.
    - **Ciclo:** Patrones de largo plazo influenciados por factores económicos o naturales, que no son necesariamente periódicos.
    - **Ruido:** Variabilidad aleatoria que no puede explicarse por los otros componentes.
""")

st.image('2024_ts_decompose.png', width=800)

st.subheader("Métodos de Forecasting")
st.write("""
    Existen varios métodos para realizar forecasting de series temporales, cada uno con sus ventajas y limitaciones. Aquí presentamos algunos de los más comunes:
""")

st.markdown("""
**1. Modelos ARIMA (AutoRegressive Integrated Moving Average)**

Los modelos ARIMA son populares por su capacidad para modelar y prever datos con tendencia y estacionalidad. Un modelo ARIMA se define por tres parámetros: p (número de términos autorregresivos), d (diferenciación para hacer la serie estacionaria) y q (número de términos de media móvil).

**2. Suavizamiento Exponencial**

Este método utiliza promedios ponderados de valores pasados, donde los valores más recientes tienen más peso. El suavizamiento exponencial puede manejar componentes de tendencia y estacionalidad, y se subdivide en métodos como SES (Simple Exponential Smoothing), Holt’s Linear Trend Model, y Holt-Winters Seasonal Model.

**3. Modelos de Machine Learning**

Con el auge del machine learning, los modelos como las Redes Neuronales y los Random Forests han demostrado ser efectivos para el forecasting de series temporales. Estos modelos pueden capturar complejas relaciones no lineales en los datos.

**4. Redes Neuronales Recurrentes (RNN) y LSTM**

Las RNN y sus variantes como LSTM (Long Short-Term Memory) son especialmente útiles para series temporales debido a su capacidad para mantener la memoria a lo largo del tiempo. Son utilizadas para modelar datos secuenciales y han mostrado excelentes resultados en la predicción de series temporales.
""")

st.subheader("Aplicaciones Prácticas")
st.write("""
    El forecasting de series temporales tiene aplicaciones prácticas en muchas áreas:
    - **Finanzas:** Predicción de precios de acciones, tipos de cambio y tendencias del mercado.
    - **Ventas y Marketing:** Previsión de la demanda de productos, planificación de inventarios y campañas de marketing.
    - **Energía:** Predicción de la demanda energética para optimizar la producción y distribución.
    - **Salud:** Predicción de brotes de enfermedades y planificación de recursos hospitalarios.
    - **Climatología:** Predicción del clima y fenómenos meteorológicos extremos.
""")

st.subheader("Caso de Estudio: Previsión de Ventas de una Tienda")
st.write("""
    Consideremos una tienda minorista que desea prever sus ventas mensuales para optimizar su inventario. Utilizando datos históricos de ventas, aplicamos un modelo ARIMA
    para identificar patrones de tendencia y estacionalidad. Tras ajustar el modelo y validar sus predicciones con datos recientes, la tienda puede anticipar picos de demanda
    y ajustar sus pedidos en consecuencia, reduciendo costos y mejorando la satisfacción del cliente.
""")

st.subheader("Conclusión")
st.write("""
    El forecasting de series temporales es una herramienta poderosa que, cuando se aplica correctamente, puede proporcionar valiosas predicciones que informan la toma de decisiones estratégicas.
    Desde métodos estadísticos tradicionales hasta avanzados algoritmos de machine learning, las técnicas de forecasting continúan evolucionando,
    ofreciendo nuevas oportunidades para entender y anticipar el comportamiento de los datos a lo largo del tiempo.
""")

st.subheader("Referencias y Recursos")
st.write("""
    - [Libro: "Forecasting: Principles and Practice" por Rob J Hyndman y George Athanasopoulos](https://otexts.com/fpp3/)
    - [Tutoriales en línea sobre ARIMA y técnicas de suavizamiento exponencial en DataCamp](https://www.datacamp.com/)
    - [Implementación de modelos LSTM para series temporales en TensorFlow](https://www.tensorflow.org/tutorials/structured_data/time_series)
""")