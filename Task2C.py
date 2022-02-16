from turtle import update
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

def run():
    '''Requirements for Task 2C'''
    stations=build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.typical_range_consistent() == False:
            stations.remove(station)
    update_water_levels(stations)
    list=stations_highest_rel_level(stations,10)
    for station in list:
        print('{},{}'.format(station.name,station.relative_water_level()))
     
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
