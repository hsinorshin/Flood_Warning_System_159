from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
import datetime
from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

#moderate   3 increases and rise by 0.05
#high   5 increases and rise by 0.10
#sever  10 increases and rise by 0.20
#low    everything else

def run():
    # Build list of stations
    stations = build_station_list()
    #stations = stations[30:80]
    update_water_levels(stations)
    dt = 5
    low = []
    moderate = []
    high = []
    severe = []
    #this works, but takes forever
    
    for station in stations:
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
        if len(levels) < 10:
            stations.remove(station)
        else:
            s = len(levels)
            counter = 0
            for i in range(0,s):
                if levels[s-i-1]>levels[s-i-2]:
                    counter+=1
                else:
                    break
            if counter >= 10 and levels[s-1]-levels[s-1-counter]>0.20:
                severe.append(station.town)
                #print(station.town,'severe\n')
                #print(levels)
            elif counter >=5 and levels[s-1]-levels[s-1-counter]>0.10:
                high.append(station.town)
                #print(station.town,'high\n')
            elif counter >=3 and levels[s-1]-levels[s-1-counter]>0.05:
                moderate.append(station.town)
                #print(station.town,'moderate\n')
            else:
                low.append(station.town)
                #print(station.town,'low\n')

    print('towns at severe risk:',severe)
    print('towns at high risk:',high)
    print('towns at moderate risk:',moderate)
    print('towns at low risk:',low)
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
