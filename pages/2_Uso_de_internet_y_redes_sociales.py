import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from shapely.geometry import Point

import funciones_graficos as fg
from functions.data_functions import get_data
from functions.graphs import graph_social_media_use, growth_internet_use
from functions.widgets import select_period_sex

st.set_page_config(
    page_title="Uso de internet y redes sociales",
    layout="wide",
)

period, sex = select_period_sex()

datos = data = get_data(sex=sex, period=period)

st.write("# Uso de internet y redes sociales")

col1, col2 = st.columns(2)

with col1:
    # st.write("## Uso de internet luego de Covid-19")
    with st.container(border=True):
        growth_internet_use(data)
with col2:
    # st.write("## Uso de redes sociales/aplicaciones")
    with st.container(border=True):
        graph_social_media_use(data)
