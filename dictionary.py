#use dictionary and list
#use functions
#use random

import random

def sum(list):
    total = 0
    for p in list:
        total += p["score"]
        return total

warriors_list = [{"name":"Stephen Curry","score": 0}, {"name":"Klay Thomson","score":0},{"name":"Dreymond Green","score":0},{"name":"Andrew Bogut","score":0}]
cavs_list = [{"name":"Lebron James","score":0},{"name":"Kyrie Irving","score":0},{"name":"Kevin Love","score":0},{"name":"Mathew Dellavodova","score":0}]
time = 0

for i in range(0, 100):
    warriors_list[random.randint(0,3)]["score"] += random.randint(1,10)
    cavs_list[random.randint(0,3)]["score"] += random.randint(1,10)
    time += 6

    warriors = sum(warriors_list)
    cavs = sum(cavs_list)
    if (time == 48):
        if(warriors > cavs):
            print ("Warriors won by ", warriors - cavs)
            exit()
        elif(cavs > warriors):
            print ("Cavs won by ", cavs - warriors)
            exit()
    elif (warriors > cavs):
        print ("Warriors leading by ", warriors - cavs)
    else:
        print ("Cavs leading by ", cavs - warriors)
