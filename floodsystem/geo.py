# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from haversine import haversine, Unit
from operator import itemgetter

def stations_by_distance(stations,p):
    #this function calculates the distance between stations 
    # and coordinate and forms a list of tuples sorted by distance
    distance_list=[]
    for i in stations:
        distance= float(haversine(i.coord,p))
        dist_tuple=(i.name,distance)
        distance_list.append(dist_tuple)
        
    sorted_dlist=sorted_by_key(distance_list,1)
    
    return sorted_dlist

def stations_within_radius(stations,centre,r):
    within_r_list=[]
    for i in stations:
        distance= float(haversine(i.coord,centre))
        if distance < r:
            within_r_list.append(i.name)

    return within_r_list

def rivers_with_station(stations):

    river_set={}
    for i in stations:
        river=i.river
        river_set.add(river)
    return river_set

def stations_by_river(stations):
    river_dict={}
    for i in stations:
        station_objects=[]
        station_id=i.station_id
        measure_id=i.measure_id
        name=i.name
        coord=i.coord
        typical_range=i.typical_range
        town=i.town
        station_objects.append(station_id,measure_id,name,coord,typical_range,town)
        river_dict[i.river]=(station_objects)
    
    return river_dict

def rivers_by_station_number(stations,N):
    '''determines the N rivers with the greatest number of monitoring stations,returns list of tuples sorted 
    by number of stations'''
    river_counter_list=[]
    
    for i in stations:
        counter=0
        river=i.river
        for u in river_counter_list:
            if river in u:
                river_counter_list.remove(u)
                counter+=1
                river_tuple=(river,counter)
                river_counter_list.append(river_tuple)
            else:
                counter=1
                river_tuple=(river,counter)
                river_counter_list.append(river_tuple)
            
    sorted(river_counter_list,key=itemgetter(1))
    final_list=[]
    for x in len(stations):
        for y in river_counter_list:
            if y[1] in river.counter_list[x]== y[1] in river.counter_list[x+1] :
                final_list.append(y)

            else:
                final_list= river_counter_list[0,N] 
    
    return final_list

