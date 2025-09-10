import pandas as pd
import plotly.express as px
import streamlit as st

st.title('DASHCOVID - Um Painel de Informações sobre a COVID-19 em 2020')

st.set_page_config(page_title="DASHCOVID", layout="wide")

df = pd.read_csv('WHO_time_series.csv')

fig1 = px.line(df, 
               x = 'Date_reported', 
               y = 'Cumulative_cases',
               color = 'Country', 
               title = 'Número de Casos Acumulados por Data')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos Acumulados')
fig1.show()

df_brasil_usa_india = df.query('Country == "Brazil" or Country == "India" or Country == "United States of America"')
fig2 = px.pie(df_brasil_usa_india, values = 'Cumulative_cases',
       names = 'Country', title = 'Número de Casos Acumulados - Brasil x India x EUA')
fig2.show()

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
