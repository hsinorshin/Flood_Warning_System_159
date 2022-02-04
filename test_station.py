# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

def test_create_monitoring_station():
    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_repr():
    string = 'Station name:     some station\n   id:            test-s-id\n   measure id:    test-m-id\n   coordinate:    (-2.0, 4.0)\n   town:          My Town\n   river:         River X\n   typical range: (-2.3, 3.4445)'
    assert repr(s) == string

#def test_typical_range_consistent():

#def test_inconsistent_typical_range_stations():
