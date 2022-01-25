
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run(N):
    '''requirements for task 1E'''
    stations=build_station_list()
    print(rivers_by_station_number(stations,N)) 


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run(9)
#this function takes a long time to perform , perhaps the algorithm isn't the most efficient 