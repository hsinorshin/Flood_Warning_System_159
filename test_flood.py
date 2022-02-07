'''Unit test for flood submodule'''

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold,stations_highest_rel_level


#created test stations
s1 = MonitoringStation(
    station_id=10,
    measure_id=1,
    label='label1',
    coord=(0.1, 0.1),
    typical_range=(0,10),
    river='river1',
    town='town1')

s2 = MonitoringStation(
    station_id=11,
    measure_id=2,
    label='label2',
    coord=(0.2, 0.2),
    typical_range=(0,10),
    river='river2',
    town='town2')

s3 = MonitoringStation(
    station_id=13,
    measure_id=3,
    label='label3',
    coord=(0.3, 0.3),
    typical_range=(0,0),
    river='river3',
    town='town3')

s4 = MonitoringStation(
    station_id=14,
    measure_id=4,
    label='label4',
    coord=(0.3, 0.3),
    typical_range=(0,10),
    river='river4',
    town='town4')

stations = [s1,s2,s3,s4]

stations[0].latest_level=5
stations[1].latest_level=2
stations[2].latest_level=None
stations[3].latest_level=12

def test_stations_level_over_threshold():
    '''test function by making sure it returns tuple of station,fraction in descending order and does not consider station with insufficient data''' 
    
    list=stations_level_over_threshold(stations,0.3)
    assert list[0]==(s4,1.2)
    assert list[1]==(s1,0.5)
    assert len(list)==2

def test_stations_highest_rel_level():
    '''test function by making sure it returns N number of items of greatest latest water levl fraction in descending order'''

    list=stations_highest_rel_level(stations,3)
    assert list[0]==s4
    assert list[1]==s1
    assert list[2]==s2
    assert len(list)==3

test_stations_highest_rel_level()


