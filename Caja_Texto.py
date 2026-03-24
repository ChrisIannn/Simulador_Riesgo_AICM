import streamlit as st

st.title("Simulador de Riesgo AICM")

# Esta es la "Caja manual" que buscabas
variacion_pax = st.number_input("Introduce la variación del AICM (ej: -0.05 para -5%)", value=0.0)

elasticidad = 0.223183
# la elasticidad global se dividio entre 12 para representar el correspondiente mensual 
# elasticidad global = 2.6782
impacto = variacion_pax * elasticidad

st.metric(label="Impacto Proyectado en Cotizaciones", value=f"{impacto:.2%}")
