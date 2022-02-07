from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run():
    '''Requirements for task 2B'''
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    station_list=stations_level_over_threshold(stations,0.8)
    for station,frac in station_list:
        print('{},{}'.format(station.name,frac))
    

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()