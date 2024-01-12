import pandas as pd
import plotly.graph_objects as px
import streamlit as st


salaries_data = pd.read_csv('ds_salaries.csv')  # Reading ds_salaries data


st.header('Data Science Salaries 2023')  # Título de la página

# Agregar el botón al programa.
hist_button = st.button('Building histogram')
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.Figure()
    fig.add_trace(px.Bar(
        x=salaries_data['work_year'],
        y=salaries_data['salary_in_usd'],
        name='Data Science Salaries 2023',
        marker=dict(
            color='rgba(196, 84, 47, 0.7)',
            line=dict(color='rgba(196, 84, 47, 0.8)', width=3)
        )
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title='Data Science Salaries 2023',
        xaxis_title='Salarie by year',
        yaxis_title='Year',
        legend_title=''
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
