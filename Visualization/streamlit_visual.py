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
st.header("Trend Keyword")