
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

def stations_highest_rel_level(stations, N):
    '''Function which returns list of N stations at which water level relevant to typical range is highest,
    arranged in descending order'''
    list=[]

    for station in stations:
        water_lvl=station.relative_water_level()
        if water_lvl!=None :
            
            list.append((station,water_lvl))
    top_list=sorted_by_key(list,1,reverse=True)
    list=[station[0] for station in top_list[:N]]
    
    return(list)







        
    
      
