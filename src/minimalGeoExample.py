import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import pandas
from shapely.geometry import Point

with open("test.csv", "w") as f:
    f.write("latitude,longitude,timestamp,random1,random2,random3\n")
    f.write("1,2,3,4,5,6\n")
    f.write("7,8,9,10,11,12\n")
    f.write("13,14,3,16,17,18\n")
    f.write("19,20,9,22,23,24\n")
    f.write("25,26,3,28,29,30\n")
    f.close()

df = pandas.read_csv("test.csv", delimiter=',', skiprows=0, low_memory=False)

geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)   

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

gdf.plot(ax=world.plot(figsize=(20, 14)), marker='o', color='red', markersize=15)

plt.savefig('world.pdf')