from dataclasses import dataclass

import numpy as np

from datapoints import datapoints


@dataclass
class process_csv:
    diff_trackers: np.ndarray = None

    def process(self, path):
        """This function will go through the csv file and will find when the date stops increasing, which presumably
        means that the tracker is now for a different animal. It will then split the data into separate arrays. These will then be turned into
        datapoints objects"""

        data = datapoints()
        data.read_csv(path)

        # This is the array that will hold the indices of the datapoints where the tracker switches to a new animal (presumably)

        indices = []
        for i in range(len(data.timestamp) - 1):
            if data.timestamp[i] > data.timestamp[i + 1]:
                print(data.timestamp[i], data.timestamp[i + 1])
                indices.append(i + 1)

        # This will split the data into separate arrays
        split_latitude = np.split(data.latitude, indices)
        split_longitude = np.split(data.longitude, indices)
        split_timestamp = np.split(data.timestamp, indices)

        # This will create a list of datapoints objects
        self.diff_trackers = []
        for i in range(len(split_latitude)):
            self.diff_trackers.append(
                datapoints(split_latitude[i], split_longitude[i], split_timestamp[i])
            )

        return self.diff_trackers
