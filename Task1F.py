from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations,MonitoringStation

def run():
    stations=build_station_list()
    list=[]
    for x in inconsistent_typical_range_stations(stations):
        station = x.name
        list.append(station)
    print(list)
   
run()