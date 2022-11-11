import os
import pytest
import Core.datapoints as dp
#use pytest to run this test

@pytest.fixture
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
        
    dp.datapoints.read_csv(dp.datapoints, 'test.csv')
    assert(dp.datapoints.latitude == [1,7,13,19,25])
    assert dp.datapoints.longitude == [2,8,14,20,26]
    assert dp.datapoints.timestamp == [3,9,15,21,27]
