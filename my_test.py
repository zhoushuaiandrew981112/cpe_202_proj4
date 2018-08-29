from bucketlist import *
from math import *

def op():
    with open("airports.csv") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip().split(','))


def hash_collision_finder():
    size = 10000
    table = CountryTable(size)
    for u in range(97, 123):
        for v in range(97, 123):
            for x in range(97, 123):
                for y in range(97, 123):
                    code_1 = chr(u) + chr(v)
                    code_2 = chr(x) + chr(y)
                    if table.hash(code_1) == table.hash(code_2) and code_1 != code_2:
                        print("code_1 :", code_1, "h_i =", table.hash(code_1), end=" | ")
                        print("code_2 :", code_2, "h_i =", table.hash(code_2), "rehash =", table.rehash(table.hash(code_2)))

hash_collision_finder()            

