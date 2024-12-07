import os
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.patches as mpatches
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(layout="wide")
st.title('Dataset Analysis')

# Load the dataset
@st.cache_data
def load_data(file):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file)
    return pd.read_csv(file_path)

df_trend = load_data('merged_trend_data.csv')
df_area = load_data('merged_area_data.csv')

# 1. Trend Keyword
st.header("1. Scopus Trend")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Keyword Trend")

    fig_line = go.Figure()

    # Add lines with labels
    fig_line.add_trace(go.Scatter(x=df_trend['Year'], y=df_trend['Count'][df_trend['Keyword'] == 'Machine Learning'], mode='lines+markers', name='Machine Learning'))
    fig_line.add_trace(go.Scatter(x=df_trend['Year'], y=df_trend['Count'][df_trend['Keyword'] == 'COVID-19'], mode='lines+markers', name='COVID-19'))
    fig_line.add_trace(go.Scatter(x=df_trend['Year'], y=df_trend['Count'][df_trend['Keyword'] == 'Climate Change'], mode='lines+markers', name='Climate Change'))
    fig_line.add_trace(go.Scatter(x=df_trend['Year'], y=df_trend['Count'][df_trend['Keyword'] == 'HIV'], mode='lines+markers', name='HIV'))
    fig_line.add_trace(go.Scatter(x=df_trend['Year'], y=df_trend['Count'][df_trend['Keyword'] == 'Hadron-Hadron scattering (experiments)'], mode='lines+markers', name='Hadron Scattering'))
    fig_line.add_trace(go.Scatter(x=df_trend['Year'], y=df_trend['Count'][df_trend['Keyword'] == 'Inflammation'], mode='lines+markers', name='Inflammation'))

    fig_line.update_layout(
        title='Keyword Trend of Scopus from 2018-2023',
        xaxis_title='Year',
        yaxis_title='Amount of Scopus',
        autosize=True,
    )

    st.plotly_chart(fig_line)

with col2:
    st.subheader("Subject Area Trend")

    fig_line = go.Figure()

    # Add lines with labels
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'MEDI'], mode='lines+markers', name='MEDI'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'ENGI'], mode='lines+markers', name='ENGI'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'COMP'], mode='lines+markers', name='COMP'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'BIOC'], mode='lines+markers', name='BIOC'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'CHEM'], mode='lines+markers', name='CHEM'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'MATE'], mode='lines+markers', name='MATE'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'ENVI'], mode='lines+markers', name='ENVI'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'AGRI'], mode='lines+markers', name='AGRI'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'PHYS'], mode='lines+markers', name='PHYS'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'SOCI'], mode='lines+markers', name='SOCI'))
    fig_line.add_trace(go.Scatter(x=df_area['Year'], y=df_area['Count'][df_area['Subject_Area'] == 'ENER'], mode='lines+markers', name='ENER'))

    fig_line.update_layout(
        title='Subject Area Trend of Scopus from 2018-2023',
        xaxis_title='Year',
        yaxis_title='Amount of Scopus',
        autosize=True,
    )

    st.plotly_chart(fig_line)