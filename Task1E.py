
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run(N):
    '''Returns the N rivers with highest number of stations. If the Nth and N+1th (and N+2th ...) have the same number, they are included as well'''
    stations=build_station_list()
    print(rivers_by_station_number(stations,N)) 


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run(12)
#this function takes a long time to perform , perhaps the algorithm isn't the most efficient 
