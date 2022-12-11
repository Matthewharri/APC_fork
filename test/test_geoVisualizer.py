import os

from src.datapoints import datapoints
from src.geoVisualizer import geoVisualizer


def test_geoVisualizer():
    """Test geoVisualizer with dummy .csv file of latitude/longitude points."""
    with open("test.csv", "w") as f:
        f.write("latitude,longitude,timestamp,random1,random2,random3\n")
        f.write("1,2,3,4,5,6\n")
        f.write("7,8,9,10,11,12\n")
        f.write("13,14,3,16,17,18\n")
        f.write("19,20,9,22,23,24\n")
        f.write("25,26,3,28,29,30\n")
        f.close()

    mypoints = datapoints()
    mypoints.read_csv("test.csv")
    myGeo = geoVisualizer(mypoints)

    # Create the plot
    outName = "plot.pdf"
    myGeo.plot(outName)

    # Check that it exists
    assert os.path.exists(outName)

    os.remove("test.csv")
    os.remove("plot.pdf")
