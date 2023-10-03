import geopandas as gpd
import requests
from shapely.geometry import Point
from pyproj import Transformer
postcode_to_check = "EH6 6JH"


# Load the SHP file into a GeoDataFrame
shp_file_path = 'pub_sca.shp'
gdf = gpd.read_file(shp_file_path, crs='EPSG:27700')
transformer = Transformer.from_crs('EPSG:4326', 'EPSG:27700', always_xy=True)

#Get coordinates from postcode
def get_coordinates_for_postcode(postcode):
    api_url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data["result"]["latitude"], data["result"]["longitude"]
    raise Exception(f"Failed to retrieve coordinates for postcode {postcode}")

try:
    latitude, longitude = get_coordinates_for_postcode(postcode_to_check)
except Exception as e:
    print(e)

# Transform the point to the same CRS as the GeoDataFrame
point = Point(transformer.transform(longitude, latitude))

# Check if the point is within any of the geometries in the GeoDataFrame
is_within_area = gdf.geometry.contains(point).any()

# Display the result
if is_within_area:
    print(f"The postcode {postcode_to_check} is within a smoke control area.")
else:
    print(f"The postcode {postcode_to_check} is not within a smoke control area.")
