import pandas as pd
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv(
    '/home/manuel-ubuntu/repositorios/Proyecto_SP7/vehicles_us.csv')

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')
# Sample
sample_df = car_data.sample(n=5000, random_state=42)

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Crear otro botón en la aplicación Streamlit
disp_button = st.button('Construir Diagrama de dispersion')

# Crear otro botón en la aplicación Streamlit
df_button = st.button('Desplegar muestra del DataFrame')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=sample_df['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


if disp_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de unDiagrama de Dispersion para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(
        data=[go.Scatter(x=sample_df['odometer'], y=sample_df['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

if df_button:
    st.write(car_data.sample(n=25))
