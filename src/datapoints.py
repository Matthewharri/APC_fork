import pandas as pd
import numpy as np
import os
from dataclasses import dataclass

@dataclass
class datapoints:
    longitude: np.ndarray
    latitude: np.ndarray
    timestamp: np.ndarray

    def read_csv(self, path):
        try:
            if(path.endswith('.csv')):
                df = pd.read_csv(path)
                column_names = list(df.columns)
                for column in column_names:
                    '''This is kind of questionable as if any of these appears in other names it will probably fail
                    but I'm trying to cover the cases if the column name is latitude or longitude withot writing several
                    statements. maybe we can talk about this more at some point'''
                    if("lat" in column):
                        self.latitude = df.pop(column).to_numpy()
                    elif("long" in column):
                        self.longitude = df.pop(column).to_numpy()
                    elif("time" in column):
                        self.timestamp = df.pop(column).to_numpy()
            elif(path.endswith('.xsl')):
                df = pd.read_excel(path)
                column_names = list(df.columns)
                for column in column_names:
                    if("lat" in column):
                        self.latitude = df.pop(column).to_numpy()
                    elif("long" in column):
                        self.longitude = df.pop(column).to_numpy()
                    elif("time" in column):
                        self.timestamp = df.pop(column).to_numpy()
            else:
                raise Exception("This file type is not supported currently. Please use .csv or .xsl")

        except FileNotFoundError:
            raise FileNotFoundError("File not found. Please check the path and try again")

def test_read_csv():
    # Create a test file of depth 5, first using the full names of the columns
    with open('test.csv', 'w') as f:
        f.write('latitude,longitude,timestamp,random1,random2,random3\n') 
        f.write('1,2,3,4,5,6\n')
        f.write('7,8,9,10,11,12\n')
        f.write('13,14,15,16,17,18\n')
        f.write('19,20,21,22,23,24\n')
        f.write('25,26,27,28,29,30\n')
        f.close()

        #now we will load in the csv file and check it gives the expected values
    
    points = datapoints(0,0,0)
    points.read_csv('test.csv')
    assert(len(points.latitude) != 0)
    assert(len(points.longitude) != 0)
    assert(len(points.timestamp) != 0)
    assert(len(points.latitude) == len(points.longitude) == len(points.timestamp))
    assert(np.array_equal(points.latitude, np.array([1,7,13,19,25])))
    assert(np.array_equal(points.longitude, np.array([2,8,14,20,26])))
    assert(np.array_equal(points.timestamp, np.array([3,9,15,21,27])))

    os.remove('test.csv')

    #now we do the same thing but using the short names
    with open('test.csv', 'w') as f:
        f.write('lat,long,time,random1,random2,random3\n') 
        f.write('1,2,3,4,5,6\n')
        f.write('7,8,9,10,11,12\n')
        f.write('13,14,15,16,17,18\n')
        f.write('19,20,21,22,23,24\n')
        f.write('25,26,27,28,29,30\n')
        f.close()

        #now we will load in the csv file and check it gives the expected values

    points = datapoints(0,0,0)
    points.read_csv('test.csv')
    assert(len(points.latitude) != 0)
    assert(len(points.longitude) != 0)
    assert(len(points.timestamp) != 0)
    assert(len(points.latitude) == len(points.longitude) == len(points.timestamp))
    assert(np.array_equal(points.latitude, np.array([1,7,13,19,25])))
    assert(np.array_equal(points.longitude, np.array([2,8,14,20,26])))
    assert(np.array_equal(points.timestamp, np.array([3,9,15,21,27])))

    os.remove('test.csv')


test_read_csv()
