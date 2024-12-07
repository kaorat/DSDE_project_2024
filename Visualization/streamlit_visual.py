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
def load_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'merged_trend_data.csv')
    return pd.read_csv(file_path)

df = load_data()

# 1. Trend Keyword
st.header("1. Trend Keyword")
fig_line = go.Figure()

# Add lines with labels
fig_line.add_trace(go.Scatter(x=df['Year'], y=df['Count'][df['Keyword'] == 'Machine Learning'], mode='lines', name='Machine Learning'))
fig_line.add_trace(go.Scatter(x=df['Year'], y=df['Count'][df['Keyword'] == 'COVID-19'], mode='lines', name='COVID-19'))
fig_line.add_trace(go.Scatter(x=df['Year'], y=df['Count'][df['Keyword'] == 'Climate Change'], mode='lines', name='Climate Change'))
fig_line.add_trace(go.Scatter(x=df['Year'], y=df['Count'][df['Keyword'] == 'HIV'], mode='lines', name='HIV'))
fig_line.add_trace(go.Scatter(x=df['Year'], y=df['Count'][df['Keyword'] == 'Hadron-Hadron scattering (experiments)'], mode='lines', name='Hadron Scattering'))
fig_line.add_trace(go.Scatter(x=df['Year'], y=df['Count'][df['Keyword'] == 'Inflammation'], mode='lines', name='Inflammation'))

fig_line.update_layout(
    title='Trend Keyword in 5 Years',
    xaxis_title='Year',
    yaxis_title='Scopus Amount',
    height=600, autosize=True
)

st.plotly_chart(fig_line)