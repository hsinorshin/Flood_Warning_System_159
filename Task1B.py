from fileinput import close
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run(p):
    '''requirements for task1B'''
   
    #build list of stations
    stations = build_station_list()
    #list of tuple(station,distance) sorted in ascending order
    list=stations_by_distance(stations,p)

    #extracts town name from stations list by checking if the stations name are equal
    closest_list=[(x[0],y.town,x[1]) for x in list[:10] for y in stations if x[0]==y.name]
    furthest_list=[(x[0],y.town,x[1]) for x in list[-10:] for y in stations if x[0]==y.name]
   
  
    #to extract town name from list of stations if station name matches
    #for 10 closest station
    # for x in list[:10]:
    #     for y in stations:
    #         if x[0] == y.name:
    #             town=y.town
    #     #build tuple of (station name, town, distance )        
    #     final_tuple=(x[0],town,x[1]) 
    #     closest_list.append(final_tuple)
    
    # #for 10 furthest station
    # for x in list[-10:]:
    #     for y in stations:
    #         if x[0] == y.name:
    #             town=y.town
    #     #build tuple of (station name, town, distance )        
    #     final_tuple=(x[0],town,x[1])
    #     furthest_list.append(final_tuple) 

    
    print('The 10 closest station from Cambridge city centre is {}\n'.format(closest_list))
    print('The 10 furthest station from Cambridge city centre is {}'.format(furthest_list))
   
    


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run((52.2053,0.1218))