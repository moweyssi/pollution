import streamlit as st
import geopandas as gpd
from shapely.geometry import Point
import requests
import folium
from folium.plugins import MarkerCluster
from pyproj import Transformer
from streamlit_folium import st_folium, folium_static

# Load the SHP file into a GeoDataFrame
shp_file_path = 'pub_sca.shp'
gdf = gpd.read_file(shp_file_path, crs='EPSG:27700')

# Define a transformer to convert between CRS
transformer = Transformer.from_crs('EPSG:4326', 'EPSG:27700', always_xy=True)

# Function to get the coordinates (latitude and longitude) for a UK postcode using postcodes.io API
@st.cache
def get_coordinates_for_postcode(postcode):
    api_url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data["result"]["latitude"], data["result"]["longitude"]
    raise Exception(f"Failed to retrieve coordinates for postcode {postcode}")

# Streamlit app title and input
st.title("Smoke control area checker")
postcode_to_check = st.text_input("Enter Scottish postcode to check")

if not postcode_to_check:
    st.stop()

# Get the coordinates (latitude and longitude) for the given postcode
try:
    latitude, longitude = get_coordinates_for_postcode(postcode_to_check)
except Exception as e:
    st.error(e)
    st.stop()

# Transform the point to the same CRS as the GeoDataFrame
point = Point(transformer.transform(longitude, latitude))

# Check if the point is within any of the geometries in the GeoDataFrame
is_within_area = gdf.geometry.contains(point).any()

# Display the result
if is_within_area:
    st.success(f"The postcode {postcode_to_check} is within a smoke control area.")
else:
    st.warning(f"The postcode {postcode_to_check} is not within a smoke control area.")

# Create a Folium map centered at the calculated centroid
m = folium.Map(location=[latitude, longitude], zoom_start=8)

# Add markers for the GeoDataFrame and the point
marker_cluster = MarkerCluster().add_to(m)
folium.Marker([latitude, longitude], icon=folium.Icon(color='red')).add_to(marker_cluster)

# Add all GeoDataFrame shapes as overlays to the map
for idx, row in gdf.iterrows():
    sim_geo = gpd.GeoSeries(row["geometry"]).simplify(tolerance=0.001)
    sim_geo.crs = 'EPSG:27700'
    goodcrs = sim_geo.to_crs('EPSG:4326')
    geo_json = goodcrs.__geo_interface__
    folium.GeoJson(geo_json, name=f"Shape {idx}").add_to(m)

# Display the Folium map
folium_static(m)
