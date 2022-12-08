from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class datapoints:
    longitude: np.ndarray = None
    latitude: np.ndarray = None
    timestamp: np.ndarray = None

    def read_csv(self, path):
        try:
            if path.endswith(".csv"):
                df = pd.read_csv(path)
                column_names = list(df.columns)
                for column in column_names:
                    """This is kind of questionable as if any of these appears in other names it will probably fail
                    but I'm trying to cover the cases if the column name is latitude or longitude without writing several
                    statements. maybe we can talk about this more at some point"""
                    if "lat" in column:
                        self.latitude = df.pop(column).to_numpy()
                    elif "long" in column:
                        self.longitude = df.pop(column).to_numpy()
                    elif "time" in column:
                        self.timestamp = df.pop(column).to_numpy()
                    else:
                        continue
            elif path.endswith(".xsl"):
                df = pd.read_excel(path)
                column_names = list(df.columns)
                for column in column_names:
                    if "lat" in column:
                        self.latitude = df.pop(column).to_numpy()
                    elif "long" in column:
                        self.longitude = df.pop(column).to_numpy()
                    elif "time" in column:
                        self.timestamp = df.pop(column).to_numpy()
                    else:
                        continue
            else:
                raise Exception(
                    "This file type is not supported currently. Please use .csv or .xsl"
                )

        except FileNotFoundError:
            raise FileNotFoundError(
                "File not found. Please check the path and try again"
            )

    def calculate_net_distance(self):
        """This is the haversine formula for calculating the distance between two points on a sphere.
        This is meant to find the net total distance from start to end"""

        R = 6372.8  # Earth radius in kilometers
        distance = (
            2
            * R
            * np.arcsin(
                np.sqrt(
                    np.sin(np.radians((self.latitude[0] - self.latitude[-1]) / 2)) ** 2
                    + np.cos(np.radians(self.latitude[-1]))
                    * np.cos(np.radians(self.latitude[0]))
                    * np.sin(np.radians((self.longitude[0] - self.longitude[-1]) / 2))
                    ** 2
                )
            )
        )
        return distance

    def calculate_total_distance(self):
        """This will be the total distance from the starting point to the end point"""
        latitude = self.latitude
        longitude = self.longitude

        distance = 0
        R = 6372.8  # Earth radius in kilometers
        for index in range(len(latitude) - 1):
            d = (
                2
                * R
                * np.arcsin(
                    np.sqrt(
                        np.sin(
                            np.radians(
                                (self.latitude[index] - self.latitude[index + 1]) / 2
                            )
                        )
                        ** 2
                        + np.cos(np.radians(self.latitude[index + 1]))
                        * np.cos(np.radians(self.latitude[index]))
                        * np.sin(
                            np.radians(
                                (self.longitude[index] - self.longitude[index + 1]) / 2
                            )
                        )
                        ** 2
                    )
                )
            )
            distance += d

        return distance
