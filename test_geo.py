"""Unit test for geo module"""

from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance,stations_within_radius
from haversine import haversine, Unit

#created test stations
s1 = MonitoringStation(
    station_id=10,
    measure_id=1,
    label='label1',
    coord=(0.1, 0.1),
    typical_range=(0,0),
    river='river1',
    town='town1')

s2 = MonitoringStation(
    station_id=11,
    measure_id=2,
    label='label2',
    coord=(0.2, 0.2),
    typical_range=(0,0),
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

stations = [s1,s2,s3]


def test_station_by_distance():
    '''test the station by distance function'''
    #test 1
    p = (0,0)   #centre
    sorted_dlist = stations_by_distance(stations,p)
    assert sorted_dlist[0][0]=='label1'
    assert sorted_dlist[1][0]=='label2'
    assert sorted_dlist[2][0]=='label3'

    #test 2
    p = (0.5,0.5)   #centre
    sorted_dlist = stations_by_distance(stations,p)
    assert sorted_dlist[0][0]=='label3'
    assert sorted_dlist[1][0]=='label2'
    assert sorted_dlist[2][0]=='label1'

def test_station_within_radius():
    '''test the station within radius function'''
    #test 1
    centre = (0,0)
    a = (0.15,0.15) #a point in between the stations
    r = float(haversine(a,centre))
    within_r_list = stations_within_radius(stations,centre,r)
    assert 'label1' in within_r_list
    assert 'label2' not in within_r_list
    assert 'label3' not in within_r_list

    #test 2
    centre = (0,0)
    a = (0.25,0.25) #a point in between the stations
    r = float(haversine(a,centre))
    within_r_list = stations_within_radius(stations,centre,r)
    assert 'label1' in within_r_list
    assert 'label2' in within_r_list
    assert 'label3' not in within_r_list

