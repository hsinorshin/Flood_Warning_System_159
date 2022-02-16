import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .station import MonitoringStation
from .datafetcher import fetch_measure_levels
import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    if dates == []:
        f = plt.figure()
        return f
    elif dates != []: 
        f = plt.figure()
        x = []
        for date in dates:
            x.append(matplotlib.dates.date2num(date))
        offset = x[0]
        # Find coefficients of best-fit polynomial f(x)
        p_coeff = np.polyfit(x-x[0],levels,p)

        # Convert coefficient into a polynomial
        poly = np.poly1d(p_coeff)

        # Plot original data points
        plt.plot(dates, levels, '.')

        # Plot polynomial fit at 30 points along interval
        x1 = np.linspace(x[0], x[-1], 30)
        plt.plot(x1,  poly(x1 - x[0]))
        return f
