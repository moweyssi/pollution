import streamlit as st
import geopandas as gpd
from shapely.geometry import Point
import requests
import matplotlib.pyplot as plt
import pyproj
import contextily as cx

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
        # Convert the point's coordinates to EPSG 27700
        projector = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:27700", always_xy=True)
        x, y = projector.transform(longitude, latitude)
        return x, y
    else:
        raise Exception(f"Failed to retrieve coordinates for postcode {postcode}")

# Define the UK postcode you want to check
st.text("gimmi postcode")
postcode_to_check = st.text_input("gigi")

# Get the coordinates (latitude and longitude) for the given postcode
try:
    longitude, latitude = get_coordinates_for_postcode(postcode_to_check)
    print(latitude,longitude)
except Exception as e:
    st.text(e)
    exit(1)

# Create a Shapely Point object from the postcode coordinates
point = Point(longitude, latitude)

# Check if the point is within any of the geometries in the GeoDataFrame
is_within_area = gdf.geometry.contains(point).any()
point_gdf = gpd.GeoDataFrame({'geometry': [point]}, crs='EPSG:27700')

# Create a Matplotlib figure and plot the GeoDataFrame and point
fig, ax = plt.subplots(figsize=(8, 8))
gdf.plot(ax=ax, color='blue', alpha=0.7)
point_gdf.plot(ax=ax, color='red', markersize=50, label='Target Point')
cx.add_basemap(ax)
plt.legend()
plt.title('Shapefile with a Single Point')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)

# Display the Matplotlib figure using st.pyplot()
st.pyplot(fig)

if is_within_area:
    st.text(f"The postcode {postcode_to_check} is within a smoke control area.")
else:
    st.text(f"The postcode {postcode_to_check} is not within a smoke control area.")
