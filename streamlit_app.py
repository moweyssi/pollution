import streamlit as st
import geopandas as gpd
from shapely.geometry import Point
import requests
import folium
from folium.plugins import MarkerCluster

# Streamlit app title and input
st.title("Smoke control area checker")
postcode_to_check = st.text_input("Enter Scottish postcode to check")
st.text(postcode_to_check)