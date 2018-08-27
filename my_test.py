from bucketlist import *
from math import *

def op():
    with open("airports.csv") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip().split(','))


city_node = CityNode("San Ramon", "CC", 90, 180)
node = CityNode("San Ramon", "CC", 90, 180)


city_node.add_city(node)



