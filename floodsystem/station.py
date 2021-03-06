# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        '''This method checks whether the typical range exists and is consistent'''
        if self.typical_range is None:
            return False
        elif float(self.typical_range[0]) < float(self.typical_range[1]):
            return True
        elif float(self.typical_range[0]) > 200 or float(self.typical_range[1]) > 200:
            return False
        else:
            return False

    def relative_water_level(self):
        '''Returns latest water level as a fraction of the typical range '''
        
        if self.typical_range_consistent() and self.latest_level!= None:
            low,high = self.typical_range
            return (self.latest_level-low)/(high-low)
        else:
            return None
        


def inconsistent_typical_range_stations(stations):
    '''returns list of stations which have missing/inconsistent data
    
    Inputs:
    stations : list of MonitoringStation objects
    
    Output:
    a list of stations which have missing/inconsistent typical range'''

    inconsistent_station_list=[]
    for station in stations:
        if station.typical_range_consistent()==True:
            pass
        else:
            inconsistent_station_list.append(station)
    return inconsistent_station_list

    

