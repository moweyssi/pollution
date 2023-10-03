import streamlit as st
import geopandas as gpd
from shapely.geometry import Point
import requests
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Load the SHP file into a GeoDataFrame
shp_file_path = 'pub_sca.shp'

gdf = gpd.read_file(shp_file_path)
gdf.crs = 'EPSG:27700'

# Function to get the coordinates (latitude and longitude) for a UK postcode using postcodes.io API
def get_coordinates_for_postcode(postcode):
    api_url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        latitude = data["result"]["latitude"]
        longitude = data["result"]["longitude"]
        return latitude, longitude
    else:
        raise Exception(f"Failed to retrieve coordinates for postcode {postcode}")

# Define the UK postcode you want to check
st.text("Give postcode")
postcode_to_check = st.text_input("Enter postcode")

# Get the coordinates (latitude and longitude) for the given postcode
try:
    latitude, longitude = get_coordinates_for_postcode(postcode_to_check)
    st.write(f"Latitude: {latitude}, Longitude: {longitude}")
except Exception as e:
    st.error(e)
    st.stop()

# Create a Shapely Point object from the postcode coordinates
point = Point(longitude, latitude)

# Check if the point is within any of the geometries in the GeoDataFrame
is_within_area = gdf.geometry.contains(point).any()

# Create a folium map
m = folium.Map(location=[latitude, longitude], zoom_start=12)

# Add markers for the GeoDataFrame and the point
for idx, row in gdf.iterrows():
    folium.GeoJson(row.geometry).add_to(m)

marker_cluster = MarkerCluster().add_to(m)
folium.Marker([latitude, longitude], icon=folium.Icon(color='red')).add_to(marker_cluster)

# Display the folium map using st.write
st_folium(m)

if is_within_area:
    st.success(f"The postcode {postcode_to_check} is within a smoke control area.")
else:
    st.warning(f"The postcode {postcode_to_check} is not within a smoke control area.")
