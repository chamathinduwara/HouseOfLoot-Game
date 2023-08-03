# HouseOfLoot-Game

HouseOfLoot-Game is a text-based adventure game implemented in Python. In this game, players explore a virtual house, navigate through different rooms, collect items, and solve challenges to win the game. The game is designed to showcase basic game mechanics and programming concepts while emphasizing the analysis of algorithmic complexity.

## Analyzing Algorithmic Complexity

One of the main focuses of HouseOfLoot-Game is to provide a practical example of algorithmic complexity analysis. Throughout the game's implementation, various algorithms are used to handle player movement, item collection, pathfinding, and more. By examining the complexity of these algorithms, players can gain insight into the efficiency and performance of different solutions.

## Getting Started

To play the HouseOfLoot-Game, follow these steps:

1.  Clone the repository to your local machine using the following command:

git clone https://github.com/your-username/HouseOfLoot-Game.git

2. Navigate to the project directory:

cd HouseOfLoot-Game

3. Run the game:

python main.py

## How to Play

- Use the following keys to navigate through the house:
- `n` - Move north
- `e` - Move east
- `s` - Move south
- `w` - Move west

- Special Commands:
- Press `f` to find the room where a specific item is placed.
- Press `p` to find the path to a specific room.
- Press `g` to grab an item in the current room.

- Press `q` to quit the game.


## Gameplay

Your objective in HouseOfLoot-Game is to explore the house, collect all the items placed in different rooms, and reach the final room to win. Keep an eye on your collected items and the available rooms as you navigate through the house.

## House Layout

The game's house is laid out as follows:

- `main_door`: Entry point to the house.
- `living_room`: Contains a remote control.
- `office`: Contains a pen.
- `office_bathroom`: Contains perfume.
- `gallery`: Contains a photo album.
- `dining_room`: Contains a spoon.
- `kitchen`: Contains a knife.
- `gym`: Contains earbuds.
- `sun_room`: Contains a cream bottle.
- `master_bedroom`: Contains a glass.
- `master_bathroom`: Contains soap.
- `library`: Contains a book.
- `end`: The final room.

## Code Overview

The code of HouseOfLoot-Game is organized into classes that represent different elements of the game. Here's a brief overview of the main classes and their functions:

- `Item`: Represents an item that can be collected.
- `Room`: Represents a room in the house, with navigation and item information.
- `SetPlayer`: Represents the player, including their current room and collected items.
- `Game`: The main game class that manages the game logic.

The game logic involves building the house layout, coordinating room connections, implementing player movement, information display, item collection, and pathfinding.

## Contributions

Contributions to HouseOfLoot-Game are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.
