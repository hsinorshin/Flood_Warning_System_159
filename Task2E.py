from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
import datetime
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    number = 5
    dt = 1

    #this works, but takes forever
    
    #for station in stations:
    #    dates, levels = fetch_measure_levels(
    #    station.measure_id, dt=datetime.timedelta(days=dt))
    #    if levels == []:
    #        stations.remove(station)


    for station in stations:
        if station.name == 'Letcombe Bassett':
            stations.remove(station)
    
    stations = stations_highest_rel_level(stations,number)

    a = []
    dt = 10
    print(stations)
    for station in stations:
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
        a.append(plot_water_levels(station, dates, levels))
    plt.show()
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
