from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    '''requirement for Task 1F'''
    #build list of stations
    stations=build_station_list()
    #prints out sorted list of station name which have inconsitent typical ranges
    print(sorted(station.name for station in inconsistent_typical_range_stations(stations)))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()