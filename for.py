import random

warriors = 0
cavs = 0

for i in range(0, 100):
    warriors = warriors + random.randint(1,10)
    cavs = cavs + random.randint(1, 10)
    if (warriors - cavs >= 30):
        print ("Warriors won by ", warriors - cavs)
        exit()
    elif(cavs - warriors >= 30):
        print ("Cavs won by ", cavs - warriors)
        exit()
    elif(warriors >  cavs):
        print ("Warriors leading by ", warriors - cavs)
    else:
        print ("Cavs leading by ", cavs - warriors)
