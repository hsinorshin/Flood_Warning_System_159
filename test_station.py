# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
#created test stations
s1 = MonitoringStation(
    station_id=10,
    measure_id=1,
    label='label1',
    coord=(0.1, 0.1),
    typical_range=None,
    river='river1',
    town='town1')
    
s2 = MonitoringStation(
    station_id=10,
    measure_id=1,
    label='label1',
    coord=(0.1, 0.1),
    typical_range=(1,0),
    river='river1',
    town='town1')
s3 = MonitoringStation(
    station_id=10,
    measure_id=1,
    label='label1',
    coord=(0.1, 0.1),
    typical_range=(0,1),
    river='river1',
    town='town1')

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    #test that the correct boolean returned for typical_range_consistent method
    r1=MonitoringStation.typical_range_consistent(s1)
    r2=MonitoringStation.typical_range_consistent(s2)
    r3=MonitoringStation.typical_range_consistent(s3)

    assert r1== False
    assert r2==False
    assert r3 == True
    

def test_inconsistent_typical_range_stations():
    list= [s1,s2,s3]
    inconsistent= inconsistent_typical_range_stations(list)
    
    assert s1 in inconsistent
    assert s2 in inconsistent
    assert s3 not in inconsistent 

