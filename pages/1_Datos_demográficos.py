import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from shapely.geometry import Point

import funciones_graficos as fg
from functions.data_functions import get_data
from functions.graphs import ages_graph, gender_sex_graph, map_graph, occupation_graph
from functions.widgets import select_period_sex

st.set_page_config(
    page_title="Datos demográficos",
    layout="wide",
)

period, sex = select_period_sex()

datos = data = get_data(sex=sex, period=period)

st.write("# Datos demográficos")

col1, col2 = st.columns(2)

with col1:
    # st.write("## Sexo y género")
    with st.container(border=True):
        gender_sex_graph(data)
    # st.write("## Ubicación")
    with st.container(border=True):
        map_graph(data)

with col2:
    # st.write("## Edades")
    with st.container(border=True):
        ages_graph(data, sex)

    # st.write("## Ocupación")
    with st.container(border=True):
        occupation_graph(data, sex)
