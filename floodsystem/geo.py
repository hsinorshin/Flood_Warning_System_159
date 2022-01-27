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
    '''this function calculates the distance between stations 
    and coordinate and forms a list of tuples sorted by distance'''
    distance_list=[]
    for i in stations:
        distance= float(haversine(i.coord,p))
        dist_tuple=(i.name,distance)
        distance_list.append(dist_tuple)
        
    sorted_dlist=sorted_by_key(distance_list,1)
    
    return sorted_dlist

def stations_within_radius(stations,centre,r):
    '''function which returns a list of
    the names of the stations within a certain radius from the centre'''
    within_r_list=[]
    for i in stations:
        distance= float(haversine(i.coord,centre))
        if distance < r:
            within_r_list.append(i.name)

    return within_r_list

def rivers_with_station(stations):
    '''function which returns set of rivers by stations'''
    #returns set of rivers with stations 
    river_set=set({})
    for i in stations:
        river=i.river
        river_set.add(river)
    return river_set

def stations_by_river(stations):
    '''function which returns a list of stations by a river'''
    #create empty dictionary
    river_dict={}
    #create list of river with >1 stations
    river=rivers_with_station(stations)
    
    for i in river:
        #list of station by a particular river
        station_list=[]
        #loop over stations list to find stations by a river
        for x in stations:
            if x.river==i:
                station=x.name
                station_list.append(station)
        #create key,value pair in dict of (river , list[stations])
        river_dict[i]=(station_list)
    
    return river_dict

def rivers_by_station_number(stations,N):
    '''this function determines the N rivers with
    the greatest number of monitoring stations,
    returns list of tuples sorted by number of stations'''
    river_list=[]
    #set of rivers 
    river=rivers_with_station(stations)
    for i in river:
        #length of list of stations for each river 
        river_counter= len(stations_by_river(stations)[i])
        river_tuple=(i,river_counter)
        #list of river and number of stations 
        river_list.append(river_tuple)
    #list organised in greatest number to least number of stations
    sorted_list=sorted_by_key(river_list,1,reverse=True)
    print(sorted_list)

    counter=0
    #if the last element of list has the same number as the next few ones, print more than N rivers
    for x in range(N-1,len(river)):
        if sorted_list[x][1] == sorted_list[x+1][1]:
            counter+=1
            print(counter)
        else: 
            break
    return sorted_list[:N+counter]
    
