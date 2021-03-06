from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():
    '''Gives a sorted list of stations based on alphabetcial order. Prints first 10 stations'''
     # Build list of stations
    stations = build_station_list()
    #extract number of rivers with at least one station
    rivernum=len(rivers_with_station(stations))
    #sort list in alphabetical order
    list=sorted(rivers_with_station(stations))

    print('{} stations. First 10 - {} \n'.format(rivernum,list[:10]))

def run2():
     # Build list of stations
    stations = build_station_list()
    
    river_aire=sorted(stations_by_river(stations)['River Aire'])
    river_cam=sorted(stations_by_river(stations)['River Cam'])
    river_thames=sorted(stations_by_river(stations)['River Thames'])

    print('Stations by River Aire : {}\n\nStations by River Cam: {}\n\nStations by River Thames: {}\n'.format(river_aire,river_cam,river_thames))




if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
    run2()
