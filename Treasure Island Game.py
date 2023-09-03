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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input('You\'re at the cross road. Where do yau want to go ?. Type "left" or "right"\n').lower()
if choice1 == "left":
  choice2 = input('You\'ve entered near an island do you want to "wait" or "swim"\n').lower()
  if choice2 == "wait":
    choice3 = input('You\'ve entered a room where you have to choose color of door which will decide your destiny. That will be "red", "blue" or "yellow"').lower()
    if choice3 == "red":
      print("You've been killed in a fire. YOU LOSE GAME OVER ")
    elif choice3 == "blue":
      print("You've been entered in room full of beasts. YOU LOSE GAME OVER")
    elif choice3 == "yellow":
      print("YOOHOO!!, You've discovered the treasure. YOU WIN")
    else:
      print("You've chose a door in this game which never exists")
  else:
    print("You've been attacked by an angry trout. YOU LOSE GAME OVER")
else:
  print("You've fallen into a hole. GAME OVER \n YOU LOSE")


