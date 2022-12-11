import os

from src.multiGeoVisualizer import multiGeoVisualizer
from src.process_csv import process_csv


def test_multiGeoVisualizer():
    """Test array-based input."""
    with open("test.csv", "w") as f:
        f.write("latitude,longitude,timestamp,random1,random2,random3\n")
        f.write("1,2,3,4,5,6\n")
        f.write("7,8,9,10,11,12\n")
        f.write("13,14,3,16,17,18\n")
        f.write("19,20,9,22,23,24\n")
        f.write("25,26,3,28,29,30\n")
        f.close()

    separated_data = process_csv().process("test.csv")
    assert len(separated_data) == 3

    plotNames = multiGeoVisualizer("testAnimal", separated_data).plot()
    for plotName in plotNames:
        assert os.path.exists(plotName)
        os.remove(plotName)

    os.remove("test.csv")
