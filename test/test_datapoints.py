import os

import numpy as np

from src.datapoints import datapoints as dp

# use pytest to run this test


def test_read_csv():
    # Create a test file of depth 5, first using the full names of the columns
    with open("test.csv", "w") as f:
        f.write("latitude,longitude,timestamp,random1,random2,random3\n")
        f.write("1,2,3,4,5,6\n")
        f.write("7,8,9,10,11,12\n")
        f.write("13,14,15,16,17,18\n")
        f.write("19,20,21,22,23,24\n")
        f.write("25,26,27,28,29,30\n")
        f.close()

    # now we will load in the csv file and check it gives the expected values

    points = dp()
    points.read_csv("test.csv")
    assert len(points.latitude) != 0
    assert len(points.longitude) != 0
    assert len(points.timestamp) != 0
    assert len(points.latitude) == len(points.longitude) == len(points.timestamp)
    assert np.array_equal(points.latitude, np.array([1, 7, 13, 19, 25]))
    assert np.array_equal(points.longitude, np.array([2, 8, 14, 20, 26]))
    assert np.array_equal(points.timestamp, np.array([3, 9, 15, 21, 27]))

    os.remove("test.csv")

    # now we do the same thing but using the short names
    with open("test.csv", "w") as f:
        f.write("lat,long,time,random1,random2,random3\n")
        f.write("1,2,3,4,5,6\n")
        f.write("7,8,9,10,11,12\n")
        f.write("13,14,15,16,17,18\n")
        f.write("19,20,21,22,23,24\n")
        f.write("25,26,27,28,29,30\n")
        f.close()

        # now we will load in the csv file and check it gives the expected values

    points = dp()
    points.read_csv("test.csv")
    assert len(points.latitude) != 0
    assert len(points.longitude) != 0
    assert len(points.timestamp) != 0
    assert len(points.latitude) == len(points.longitude) == len(points.timestamp)
    assert np.array_equal(points.latitude, np.array([1, 7, 13, 19, 25]))
    assert np.array_equal(points.longitude, np.array([2, 8, 14, 20, 26]))
    assert np.array_equal(points.timestamp, np.array([3, 9, 15, 21, 27]))

    os.remove("test.csv")
    """I don't think a test is needed for reading in the .xsl files since it is an identical test to the .csv files,
    But i can add them in if anyone thinks it is needed"""

    # now we will test the exception handling
    try:
        points.read_csv("test.csv")
        assert False
    except FileNotFoundError:
        assert True


def test_calculate_net_distance():
    with open("test.csv", "w") as f:
        f.write("lat,long,time,random1,random2,random3\n")
        f.write("1,2,3,4,5,6\n")
        f.write("7,8,9,10,11,12\n")
        f.write("13,14,15,16,17,18\n")
        f.write("19,20,21,22,23,24\n")
        f.write("25,26,27,28,29,30\n")
        f.close()

    points = dp()
    points.read_csv("test.csv")
    assert points.calculate_net_distance() - 3710 <= 1

    os.remove("test.csv")


def test_calculate_total_distance():
    with open("test.csv", "w") as f:
        f.write("lat,long,time,random1,random2,random3\n")
        f.write("1,2,3,4,5,6\n")
        f.write("7,8,9,10,11,12\n")
        f.write("13,14,15,16,17,18\n")
        f.write("19,20,21,22,23,24\n")
        f.write("25,26,27,28,29,30\n")
        f.close()

    points = dp()
    points.read_csv("test.csv")
    assert points.calculate_total_distance() - 942.2 - 936.2 - 925.2 - 909.5 <= 1

    os.remove("test.csv")
