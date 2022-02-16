from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
import datetime
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    number = 5
    stations = stations_highest_rel_level(stations,number)
    #print(stations)
    dt = 10
    a = []
    #print(stations)
    for station in stations:
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
        a.append(polyfit(dates, levels,3))
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(station.name)
        plt.tight_layout() 
    plt.show()
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
