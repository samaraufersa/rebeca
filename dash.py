import pandas as pd
import plotly.express as px
import streamlit as st

st.title('DASHCOVI - Um Painel de Informações sobre a COVID-19 em 2020')

st.set_page_config(page_title="DASHCOVID", layout="wide")

df = pd.read_csv('WHO_time_series.csv')

fig1 = px.line(df, 
               x = 'Date_reported', 
               y = 'Cumulative_cases',
               color = 'Country', 
               title = 'Número de Casos Acumulados por Data')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Número de Casos Acumulados')
fig1.show()

st.plotly_chart(fig1, use_container_width=True)
