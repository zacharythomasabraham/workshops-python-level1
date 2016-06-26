#create two lists
#use while to let user enter player
#check list1 and list2
#print messages

warriors = ["Stephen Curry", "Klay Thomson", "Dreymond Green" , "Andrew Bogut"]
cavs = ["Lebron James", "Kyrie Irving", "Kevin Love" , "Mathew Dellavodova"]

while(True):
    player = raw_input("Enter a player's name?")

    if player in warriors:
        print player + "is on the Warriors\n"
        exit()
    elif player in cavs:
        print player + "is on the Cavs\n"
        exit()
    else:
        print player + "not found\n"
