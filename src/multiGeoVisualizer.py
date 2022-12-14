from dataclasses import dataclass
from typing import List

import geopandas
import matplotlib.pyplot as plt
import pandas
import wikipedia
from geopandas import GeoDataFrame
from shapely.geometry import Point

from geoVisualizer import geoVisualizer
from process_csv import process_csv


@dataclass
class multiGeoVisualizer:
    nTracks: int
    animalName: str
    geoVisList: List[geoVisualizer]

    def __init__(self, animalName: str, inputTracks: process_csv):
        """Initialize a multiGeoVisualizer object using the process_csv class as input."""

        if len(inputTracks) == 0:
            raise Exception("Input list has no elements!")

        self.nTracks = len(inputTracks)
        self.animalName = animalName
        print("Found", self.nTracks, "tracks for", self.animalName)
        print("From wikipedia.org: ")
        print(wikipedia.summary(self.animalName))

        self.geoVisList = [geoVisualizer(track) for track in inputTracks]

    def plot(self):
        """Plot all available tracks to different files

        Returns
        ------
        A list of the output plot names.
        """
        plotNames = []
        for i in range(self.nTracks):
            plotName = f"plotTrack_{i}.pdf"
            self.geoVisList[i].plot(plotName)
            print("Creating", plotName, "...")
            plotNames.append(plotName)
        return plotNames
