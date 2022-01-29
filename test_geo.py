"""Unit test for geo module"""

from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance,stations_within_radius,rivers_with_station,stations_by_river,rivers_by_station_number
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
    '''test the station by distance function using known stations'''
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
    '''test the station within radius function
    by checking whether the correct results are in the list'''
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

def test_rivers_with_station():
    '''test the rivers with station function
    by checking whether the set is correctly created'''
    river_set=rivers_with_station(stations)
    assert river_set=={'river1','river2','river3'}

#New stations for testing
s4 = MonitoringStation(
    station_id=13,
    measure_id=3,
    label='label4',
    coord=(0.3, 0.3),
    typical_range=(0,0),
    river='river1',
    town='town1')
s5 = MonitoringStation(
    station_id=13,
    measure_id=3,
    label='label5',
    coord=(0.3, 0.3),
    typical_range=(0,0),
    river='river1',
    town='town1')
s6 = MonitoringStation(
    station_id=13,
    measure_id=3,
    label='label6',
    coord=(0.3, 0.3),
    typical_range=(0,0),
    river='river2',
    town='town2')

stations_2 = [s1,s2,s3,s4,s5,s6]

def test_stations_by_river():
    '''test the stations by river function'''
    river_dict = stations_by_river(stations_2)
    should_be = {'river1': ['label1', 'label4', 'label5'],'river2': ['label2', 'label6'], 'river3': ['label3']}
    assert river_dict == should_be

#even more stations,
    #1,4,5 are river1
    #2,6,7 are river2
    #3 is river 3
    #8,9,10,11 are river 4
    
s7 = MonitoringStation(
    station_id=13,
    measure_id=3,
    label='label7',
    coord=(0.3, 0.3),
    typical_range=(0,0),
    river='river2',
    town='town2')
s8 = MonitoringStation(
    station_id=13,
    measure_id=3,
    label='label8',
    coord=(0.3, 0.3),
    typical_range=(0,0),
    river='river4',
    town='town4')
s9 = MonitoringStation(
    station_id=13,
    measure_id=3,
    label='label9',
    coord=(0.3, 0.3),
    typical_range=(0,0),
    river='river4',
    town='town4')
s10 = MonitoringStation(
    station_id=13,
    measure_id=3,
    label='label10',
    coord=(0.3, 0.3),
    typical_range=(0,0),
    river='river4',
    town='town4')
s11 = MonitoringStation(
    station_id=13,
    measure_id=3,
    label='label11',
    coord=(0.3, 0.3),
    typical_range=(0,0),
    river='river4',
    town='town4')

stations_3 = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11]

def test_rivers_by_station_number():
    '''test the rivers by station function'''
    a = rivers_by_station_number(stations_3,1)  #test with maximum
    assert a==[('river4', 4)]
    b = rivers_by_station_number(stations_3,2)  #test that when the multiple rivers have the lowest, all are displayed
    assert len(b)==3
    assert b[1][0]=='river2' or 'river1'
    assert b[2][0]=='river2' or 'river1'
    assert b[2][0] != b[1][0]
