from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run(centre,r):
     #build list of stations
    stations = build_station_list()

    #create sorted list of stations which radius r of coordinate x
    list=sorted(stations_within_radius(stations,centre,r))
    print(list)


run( (52.2053, 0.1218),10)
