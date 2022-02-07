
from .utils import sorted_by_key  



def stations_level_over_threshold(stations,tol):
    '''Function which returns a list of tuples with stations that have water level exceeding the tolerance
    arranged in descending order'''
    
    over_tol_list=[]
    for station in stations:
        water_lvl=station.relative_water_level()
        if water_lvl!=None:
        
            if water_lvl>tol:
                
                over_tol_list.append((station,water_lvl))

        else:
            pass 

    return sorted_by_key(over_tol_list,1,reverse=True)
        
    
      
