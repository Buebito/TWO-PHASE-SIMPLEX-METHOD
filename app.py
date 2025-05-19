import streamlit as st
import numpy as np
from Simplex import simplex_estandar  # Importa tu función

st.title("Resolver Simplex con Streamlit")

# Entradas del usuario
m = st.number_input("Número de restricciones (m):", min_value=1, step=1, value=2)
n = st.number_input("Número de variables (n):", min_value=1, step=1, value=3)

matriz_input = st.text_area(
    "Ingrese la matriz A (separando filas con líneas nuevas):", 
    value="1 2 3\n4 5 6"
)
costos_input = st.text_input("Ingrese el vector de costos:", value="7 8 9")
recursos_input = st.text_input("Ingrese el vector de recursos:", value="10 11")

debug = st.checkbox("Modo Debug", value=False)

if st.button("Resolver"):
    try:
        matriz = np.array([list(map(float, row.split())) for row in matriz_input.split('\n')])
        costos = np.array(list(map(float, costos_input.split()))).reshape(1, -1)
        recursos = np.array(list(map(float, recursos_input.split()))).reshape(-1, 1)

        # Llamamos a la función simplex_estandar desde Simple.py
        resultado = simplex_estandar(m, n, matriz, costos, recursos, debug=debug)

        st.success("¡Problema resuelto!")
        st.write("**Tabla final:**")
        st.write(resultado[0])
        st.write("**Solución óptima:**", resultado[1])
        st.write("**Valor de la función objetivo:**", resultado[2])
    except Exception as e:
        st.error(f"Hubo un error: {e}")
