from math import *

with open("airports.csv") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip().split(','))
