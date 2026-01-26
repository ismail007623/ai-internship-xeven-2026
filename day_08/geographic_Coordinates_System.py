import math

cities = [
    ('karachi', 24.8607, 67.0011),
    ('sahiwal',30.6612, 73.1085),
    ('multan',30.1864, 71.4886),
    ('okara',30.8154,73.4526)
]


def calculate_distance(target_location , city):
    """    
    Args :
    tuple_1: 
    tuple_2: 
    """
    
    try :

        earth_distnace = 6371
        name1, latitude1, longitude1 = city
        name2, latitude2, longitude2 = target_location

        print(f"City : {name1} : latitude : {latitude1} : logitude: {longitude1}")
        print(f"City : {name2} : latitude : {latitude2} : logitude: {longitude2}")

        latitude1 = math.radians(latitude1)
        longitude1 = math.radians(longitude1)
        latitude2 = math.radians(latitude2)
        longitude2 = math.radians(longitude2)

        latitude_difference = latitude1 - latitude2
        longitude_difference = longitude1 - longitude2

        a = math.sin(latitude_difference / 2)**2 + \
        math.cos(latitude1) * math.cos(latitude2) * \
        math.sin(longitude_difference / 2)**2

        # 3. Calculate Angular Distance (c)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = earth_distnace * c

        return distance

    except ValueError:
        print("tuple must contain 3 parameters")


def find_close_city(target_location , coardinate):
    """
    Docstring for find_close_city
    
    :param target_location: Description
    :param coardinate: Description
    """
    try:
        clostest_city = None
        minimum_distance = float ('inf')

        for city in coardinate :
            distance = calculate_distance(target_location ,city)

            if distance < minimum_distance :
                minimum_distance = distance
                clostest_city = city[0]

        return (clostest_city , minimum_distance)
    
    except ValueError:
        print("Error : tuple must contain 3 value city name , latitude , logitude")


if __name__ == "__main__":
  location = ('lahore', 31.5204 , 74.3587)
  result = find_close_city(location , cities)
  print(f"the clostest city : {result[0]} at : {result[1]}  km")
    

        



