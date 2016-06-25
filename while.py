# Get the score from user
# Tell the user what the lead is
# Only terminates if warriors score greater than cavs by 30


while(True):
    warriors = int(input("What is the warriors score?"))
    cavs = int(input("What is the cavs score?"))
    if(warriors - cavs >= 30):
        print ("Warriors won by ", warriors - cavs)
        exit()
    else:
        print ("Warriors leading by ", warriors - cavs)
