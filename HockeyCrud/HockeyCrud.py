listOfPlayers = []

class Player:
    Namn = ""
    JerseyNumber = 0
    Goals = 0
    Assists = 0

def CreatePlayer():
    print("*** New player ***")
    newPlayer = Player()
    newPlayer.Namn = input("Name:")
    newPlayer.JerseyNumber = int(input("JerseyNumber"))
    return newPlayer

def SelectOnePlayer():
    print("Select one player")
    nr = 1
    for player in listOfPlayers:
        print(f"{nr} {player.Namn} {player.JerseyNumber}")
        nr = nr + 1
    selection = int(input("Välj ->"))
    return listOfPlayers[selection-1]

def UpdatePlayer(player):
    print(f"Update player {player.Namn} ")
    print(f"Enter a new value of leave blank if no change")
    namn = input(f"Namn (existing={player.Namn})")
    if namn != "":
        player.Namn = namn
    jersey = input(f"Jersey (existing={player.JerseyNumber})")
    if jersey != "":
        player.JerseyNumber = int(jersey)
    goals = input(f"Goals (existing={player.Goals})")
    if goals != "":
        player.Goals = int(goals)
    assists = input(f"Assists (existing={player.Assists})")
    if assists != "":
        player.Assists = int(assists)

def SearchPlayers():
    searchWord = input("Enter what to search for")
    for player in listOfPlayers:
        if player.Namn.upper().find(searchWord.upper()) != -1:
            print(f"{player.Namn} {player.JerseyNumber}")


while True:
    print("1. New player")
    print("2. List all player")
    print("3. Update player")
    print("4. Delete player")
    print("5. Search player")
    print("6. Exit")
    selection = input("Välj ->")
    if selection == "1":
        listOfPlayers.append(CreatePlayer())
    elif selection == "2":
        for player in listOfPlayers:
            print(f"{player.Namn} {player.JerseyNumber}")
    elif selection == "3":
        playerToUpdate = SelectOnePlayer()
        UpdatePlayer(playerToUpdate)
    elif selection == "4":
        playerToUpdate = SelectOnePlayer()
        listOfPlayers.remove(playerToUpdate)
    elif selection == "5":
        SearchPlayers()
    elif selection == "6":
        break