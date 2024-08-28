"""
Treasure Island Game

Author: Alan
Date: August 21th 2024

This is a simple text-based adventure game where the player makes choices to find a hidden treasure on an island.
The player will be prompted to choose directions and actions, and the outcome will be determined based on their choices.
"""

# Print the game introduction and map
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First choice: left or right
direction = input("Where should we go on this island? (left/right): ").lower()

# Decision tree based on the player's choices
if direction == "left":
    # Second choice: swim or wait
    direction = input("We are at the shore, should we swim or wait? (swim/wait): ").lower()
    if direction == "wait":
        # Third choice: pick a door
        direction = input("Behind you, there are three doors! Which one should we open? (red/blue/yellow): ").lower()
        if direction == "yellow":
            print("Congrats! You found the treasure, you won!")
        else:
            print("Sorry! Game over!")
    else:
        print("Sorry! Game over!")
else:
    print("Sorry! Game over!")
