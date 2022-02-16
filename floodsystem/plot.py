import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .station import MonitoringStation
from .datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):

    f = plt.figure()
    # Plot
    plt.plot(dates, levels)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    
    return f
        
