from dataclasses import dataclass

import geopandas
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import pandas
from shapely.geometry import Point
from typing import List

from datapoints import datapoints


@dataclass
class geoVisualizer:
    inDataFrame: pandas.DataFrame
    geometry: List[Point]
    geoDataFrame = GeoDataFrame

    def __init__(self, data: datapoints):
        """Initialize a geoVisualizer object using the datapoints class as input."""
        if (data.latitude is None) or (data.longitude is None):
            raise Exception(
                "Input data did not have valid latitude and longitude fields"
            )

        if len(data.latitude) != len(data.longitude):
            raise Exception(
                "Number of latitude points does not match number of longitude points"
            )

        # Cast the datapoints class to a pandas DataFrame
        self.inDataFrame = pandas.DataFrame(
            {"latitude": data.latitude, "longitude": data.longitude}
        )
        # Use Shapely Point object to make geometry for GeoDataFrame constructor
        self.geometry = [
            Point(xy)
            for xy in zip(self.inDataFrame["longitude"], self.inDataFrame["latitude"])
        ]
        # Call GeoDataFrame constructor
        self.geoDataFrame = GeoDataFrame(self.inDataFrame, geometry=self.geometry)

    def plot(self, outName: str):
        """Plot the lat/long points on a world map and save the plot.

        Parameters
        ----------
        outName : str
            Path/name of output file.

        Returns
        ------
        none
        """
        world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
        self.geoDataFrame.plot(
            ax=world.plot(figsize=(20, 14)), marker="o", color="red", markersize=15
        )
        plt.savefig(outName)
