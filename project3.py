print("Welcome to Treasure Island.\nYour mission is to find treasure.")
one = input("You're at a cross road. Where do you want to go? left or right? ")
if one == "left":
    two = input("You have come to a lake. There is an island in the middle of the lake. Do you want to swim or wait? ")

    if two == "wait":
        three = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, One blue, and one yellow. Which one do you choose? ")
        
        if three == "red":
            print("You found treasure!")
        else:
            print("Mission Failed.")
    else:
        print("Mission Failed")
else:
    print("Mission Failed!")

