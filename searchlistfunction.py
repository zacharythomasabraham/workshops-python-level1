warriors = ["Stephen Curry", "Klay Thomson", "Dreymond Green" , "Andrew Bogut"]
cavs = ["Lebron James", "Kyrie Irving", "Kevin Love" , "Mathew Dellavodova"]

def search(value):
    if value in warriors:
        print value + "is on the Warriors\n"
        exit()
    elif value in cavs:
        print value + "is on the Cavs\n"
        exit()
    else:
        print value + "not found\n"


while(True):
    player = raw_input("Enter a player's name?")
    search(player)
