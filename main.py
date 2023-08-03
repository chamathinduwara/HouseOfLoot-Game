# import house data 
from house import house

# create empty lists to store room and item objects
room_list = []
Item_List = []

# create item class
class Item:
    
    def __init__(self,name,room):
        # O(1) - constant time complexity
        # initialize name and room attributes
        self.name = name
        self.room = room

# create room class
class Room():

    def __init__(self, name=None, north=None, east=None, south=None, west=None, item=None) :
        # O(1) - constant time complexity
        # initialize name and room attributes
        self.name = name
        self.north = north
        self.east = east
        self.south =south
        self.west = west
        self.item = item

# create player class
class SetPlayer:
    
    def __init__(self, name='player1', room=None, item_list=[]):
        # O(1) - constant time complexity
        # initialize name, room, and item_list attributes
        self.name = name
        self.room = room
        self.item_list = item_list


# create game class
class Game:

    def __init__(self):
        # O(1) - constant time complexity
        # initialize game instance
        pass

# build the house and add items
    def build(seif):
        # O(n) -Linear time complexity, this loop will iterate through each element in the house list
        for rm in house:
            r = Room()
            r.name = rm
            if 'item' in house[rm]:
                r.item = house[rm]['item']
                loot_item = Item(house[rm]['item'],r)
                Item_List.append(loot_item)


            room_list.append(r)

# set house coordination
    def coordination(self):
        # O(n^2) -Quadratic time complxity, this nested loop will iterate through each element in the room_list for each element in room_list
        for rm in room_list:
            for rm1 in room_list:
                if house[rm.name]['north'] == rm1.name:
                    rm.north = rm1
                elif house[rm.name]['south'] == rm1.name:
                    rm.south = rm1
                elif house[rm.name]['east'] == rm1.name:
                    rm.east = rm1
                elif house[rm.name]['west'] == rm1.name:
                    rm.west = rm1


# set player movement throughout the house
    def Move(self,player,direction):
        # O(1) -Constant time complxity, this function will always take constant time as it only performs a single operation
        if direction == 'w' and player.room.west != None:
            player.room = player.room.west
        elif direction == 's' and player.room.south != None:
            player.room = player.room.south
        elif direction == 'n' and player.room.north != None:
            player.room = player.room.north
        elif direction == 'e' and player.room.east != None:
            player.room = player.room.east
        else:
            print('___wrong command !!!___ please read instructions')
            
# set player information
    def information(self,player,count):
        # O(1) - Constant time complexity, this function will always take constant time
        how_to_play = """***Welcome to Adventure loot finding game*** \n
        Your target is to find the all items before going to the end \n

        you can move around the house using "n", "e", "s", "w" keys.
        n - north
        e - east
        s - south
        w - west

        you have two ability
        using 'f' you can find the room of item placed in
        using 'p' you can find the path to go to a room
        using 'g' you can grab the item

        press 'q' to quit from the game
        """
        if count == 'start':
            print(how_to_play)

            print("item list :-")
            for item in Item_List:
                print(item.name,end=" ,")
            print("\n room list :-")
            for room in room_list:
                print(room.name,end=' ,')
            print("\n")
            print(player.name,"your current room is : ", player.room.name)

        # 
        if count == 'go':
            print(player.name,"your current room is : ", player.room.name," -  items in this room :",player.room.item)
            print(player.name,"you collected this items : " ,player.item_list)
    
            print("you can go from here : ")
            if player.room.north != None:
                print('n : ' ,player.room.north.name)
            if player.room.east != None:
                print('e : ',player.room.east.name)
            if player.room.south != None:
                print('s : ', player.room.south.name)
            if player.room.west != None:
                print('w : ', player.room.west.name)



# find room that item is placed
    def find_loot(self):
        # O(n) - Liner time complexcity, this loop will iterate through each element in the Item_List
        item_name = input("Enter item name you want to find : ")

        for item in Item_List:
            if item_name == item.name:
                print("your item is in : ",  item.room.name)



# find path to a room
    def find_path(self,player):
        # O(n^2) - Quadratic time complexcity, it performs a nested loop through the room_list and PathSearch function.
        room_name = input("Enter name of the room you want to go : ")

        for r in room_list:
            if r.name == room_name:

                paths = self.path_search(player.room, room_name)

                if paths == "No path found":
                    print(paths)
                    break
                correct_path = []
                correct_dir = paths[-1][-1]
                for path in range(len(paths),0,-1):
                    if correct_dir == paths[path-1][-1]:
                        correct_path.insert(0,paths[path-1])
                        correct_dir = paths[path-1][0]
                # correct_path.insert(0,paths[0])
                print('follow this step to go to :',room_name,' \n',correct_path)

                break
        else:
            print("No such room in the house")


# set collect item
    def grab_item(self,player):
        # O(1) - Constant time complxctiy, this function take constant time as it only performs a single operation
        if player.room.item in player.item_list:
            print('you already collected this item')
        elif player.room.item == None:
            print("No item in this room")
        else:
            player.item_list.append(player.room.item)


    # search path to a specific room
    def path_search(self,currect_room,destination):
        # O(n) - linear time complexity, it performs a single operation for each room in the search_list.

        # initialize path_index and search_list with the current room
        path_index = 0
        search_list = [currect_room ]

        # initialize paths
        paths = []

        # check if the current room is the destination
        if currect_room.name == destination:
            return search_list[0]

        while True:
            # O(n) - lineat time complexity, it performs a single operation for each room in the search_list.
            # check if the adjacent rooms of the current room are the destination
            if currect_room.east != None and destination == currect_room.east.name  :
                paths.append([currect_room.name,'e',currect_room.east.name])
                return paths
            elif  currect_room.north != None and destination == currect_room.north.name :
                paths.append([currect_room.name,'n',currect_room.north.name])
                return paths
            elif  currect_room.south != None and destination == currect_room.south.name :
                paths.append([currect_room.name,'s',currect_room.south.name])
                return paths
            elif currect_room.west != None and destination == currect_room.west.name  :
                paths.append([currect_room.name,'w',currect_room.west.name])
                return paths
            else:
                # add the adjacent rooms of the current room to the search list
                if currect_room.east not in search_list and currect_room.east != None:
                    search_list.append(currect_room.east)
                    paths.append([currect_room.name,'e',currect_room.east.name])
                if currect_room.north not in search_list and currect_room.north != None:
                    search_list.append(currect_room.north)
                    paths.append([currect_room.name,'n',currect_room.north.name])
                if currect_room.south not in search_list and currect_room.south != None:
                    search_list.append(currect_room.south)
                    paths.append([currect_room.name,'s',currect_room.south.name])
                if currect_room.west not in search_list and currect_room.west != None:
                    search_list.append(currect_room.west)
                    paths.append([currect_room.name,'w',currect_room.west.name])

                # check if the search list is empty
                if len(search_list) == path_index:
                    return "No path found"
                else:
                    # update the current room and path_index
                    path_index += 1
                    currect_room = search_list[path_index]



            


        
    

        
# main function 
def play():
    # O(n^2) - Quadratic time complexity, 
    # it contains a while loop that iterates through the room_list and calls the Information, FintPath, and GrabItem functions
    # which have a quadratic time complexity.
    # create a game instance
    g= Game()
    # build the house and add items
    g.build()
    # set house coordination
    g.coordination()

    # get player name
    player_name = input("Enter your name : ")
    # create a player instance
    player1 = SetPlayer(player_name)

    # set player's starting room
    player1.room = room_list[0]

    # initialize count variable
    count = 'start'
    # while loop to run the game
    while True:
        print("\n")
        # O(n^2) - Quadratic time complexity
        # check if the player is in the end room

        if player1.room.name == 'end' :
            # check if the player has collected all the items
            if (player1.item_list) == len(Item_List):
                print("you win")
                break
            else:
                print("you loose, you were not found all the item in the house") 
                break
        # display player information and available rooms and items
        g.information(player1,count)
        # increase count by 1
        count = 'go'
        # get player's direction
        direction = str(input("enter your movement : ")).lower()

        # check if the player wants to quit the game
        if direction == 'q':
            break

        # check if the player wants to find the room of an item
        elif direction == 'f':
            # call the FindLoot function to find the room of the item
            g.find_loot()
            count = 'stop'
            # skip the rest of the loop and continue to the next iteration
            continue

        # check if the player wants to find the path to a room
        elif direction == 'p':
            # call the FindPath function to find the path to the room
            g.find_path(player1)
            count = 'stop'
            # skip the rest of the loop and continue to the next iteration
            continue


        # check if the player wants to collect an item
        elif direction == 'g':
            # call the GrabItem function to collect the item
            g.grab_item(player1)
            # skip the rest of the loop and continue to the next iteration
            continue
        else:
            # move the player to the new room
            g.Move(player1,direction)


    



if __name__=="__main__":
    play()






