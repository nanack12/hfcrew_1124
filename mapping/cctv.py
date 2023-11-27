import pandas as pd
import folium
import geopandas as gpd
import json
from folium import GeoJson, plugins

tiles = "http://mt0.google.com/vt/lyrs=m&hl=ko&x={x}&y={y}&z={z}"
attr = "Google"
map_gangseo = folium.Map(location=[37.5612346, 126.8228132], zoom_start=13, tiles=tiles, attr=attr)

map_gangseo.save("./map.html")


geojson_path = './geojson/najs.geojson'
with open(geojson_path, encoding='utf-8') as f:
    data = json.load(f)


geojson_layer = GeoJson(data, style_function=lambda x: {"fillColor": "blue",
                                                         "color": "gray",
                                                         "weight": 1,
                                                         "fillOpacity": 0.1}).add_to(map_gangseo)


GS_geoData = pd.read_csv('./csv/gangseo_cctv.csv', encoding='utf-8', engine='python')
GS_geoData.info()


heat_data = [[row['위도'], row['경도']] for index, row in GS_geoData.iterrows()]
heatmap = plugins.HeatMap(heat_data, min_opacity=0.2, max_val=1.5, radius=20, blur=20, max_zoom=1)


heatmap.add_to(map_gangseo)


map_gangseo.save('./html/cctv_final_heatmap.html')
