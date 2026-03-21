Caja_Texto_AIFA
import streamlit as st
st.set_page_config(page_title="Simulador AIFA")

st.title("Simulador de Riesgo AIFA")

# Esta es la "Caja manual" que buscabas
variacion_pax = st.number_input("Introduce la variación del AIFA (ej: -0.05 para -5%)", value=0.0)

elasticidad = 1.2489
impacto = variacion_pax * elasticidad

st.metric(label="Impacto Proyectado en Cotizaciones", value=f"{impacto:.2%}")
