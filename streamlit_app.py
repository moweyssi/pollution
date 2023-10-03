import streamlit as st
import geopandas as gpd
from shapely.geometry import Point
import requests
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from pyproj import Transformer

# Load the SHP file into a GeoDataFrame
shp_file_path = 'pub_sca.shp'

gdf = gpd.read_file(shp_file_path)
gdf.crs = 'EPSG:27700'  # Set the CRS to British National Grid (EPSG:27700)

# Define a transformer to convert between CRS
transformer = Transformer.from_crs('EPSG:4326', 'EPSG:27700', always_xy=True)

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
st.title("Smoke control area postcode checker")
st.text("Give a Scottish postcode to check")
postcode_to_check = st.text_input(None)

# Get the coordinates (latitude and longitude) for the given postcode
try:
    latitude, longitude = get_coordinates_for_postcode(postcode_to_check)
    st.write(f"Latitude: {latitude}, Longitude: {longitude}")
except Exception as e:
    st.error(e)
    st.stop()

# Transform the point to the same CRS as the GeoDataFrame
point = Point(transformer.transform(longitude, latitude))

# Check if the point is within any of the geometries in the GeoDataFrame
is_within_area = gdf.geometry.contains(point).any()
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
    sim_geo = gpd.GeoSeries(row["geometry"]).simplify(tolerance=0.002)
    sim_geo.crs = 'EPSG:27700'
    goodcrs = sim_geo.to_crs('EPSG:4326')
    geo_json = goodcrs.to_json()
    folium.GeoJson(geo_json, name=f"Shape {idx}").add_to(m)

# Display the folium map using st_folium
st_folium(m,width="full")

