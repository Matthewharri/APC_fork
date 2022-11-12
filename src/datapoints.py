from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class datapoints:
    longitude: np.ndarray
    latitude: np.ndarray
    timestamp: np.ndarray

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
