import pandas as pd
import plotly.graph_objects as px
import streamlit as st


salaries_data = pd.read_csv('ds_salaries.csv')  # Reading ds_salaries data

salaries_data['n_job_title'] = salaries_data['experience_level'].astype(
    'category').cat.codes  # Creating a numeric column from a category


st.header('Data Science Salaries 2023')  # Principal title

# Add button to the program
hist_button = st.button('Buil a Histogram')
if hist_button:  # By clicking on the button:
    # Write a message
    st.write(
        'Creating a histogram for the dataset of: Data Science Salaries 2023')

    # Creating a histogram
    fig = px.Figure()
    fig.add_trace(px.Histogram(
        x=salaries_data['salary_in_usd'],
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
        xaxis_title='Salarie in USD'
    )

    # Display an interactive Plotly chart
    st.plotly_chart(fig, use_container_width=True)

    # Add the button to the program.
scatter_button = st.button('Buil a scatter chart')
if scatter_button:  # By clicking on the button:
    # Write a message
    st.write(
        'Creating a scatter chart for the dataset of: Data Science Salaries 2023')

    # Creating a scatter chart
    fig2 = px.Figure()
    fig2.add_trace(px.Scatter(
        x=salaries_data['work_year'],
        y=salaries_data['n_job_title'],
        name='Data Science Salaries 2023',
        mode='markers'
    )
    )
    fig2.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        title='Data Science Salaries 2023',
        xaxis_title='Salarie in USD',
        yaxis_title=''
    )

    # Display an interactive Plotly chart
    st.plotly_chart(fig2, use_container_width=True)
