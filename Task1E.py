
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run(N):
    stations=build_station_list()
    print(rivers_by_station_number(stations,N)) 

run(9)

#this function takes a long time to perform , perhaps the algorithm isn't the most efficient 