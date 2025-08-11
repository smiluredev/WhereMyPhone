# Where is my Phone?
# Made By: MiguelTheDRMR

print("You forgotten your phone in some place, now you have to find it.")
print("You have: Living Room, Attic, Kitchen & Bathroom")

choice = input("What's your choice?: ")

if choice == "Living Room":
    print("You look for your phone in the Living Room, but you don't find it...")
    choice2 = input("Where will you go now? (Attic/Bathroom): ")
    
    if choice2 == "Attic":
        print("You look for your phone in the Attic, but you don't find it...")
        choice3 = input("Where will you go now? (Bathroom): ")
        if choice3 == "Bathroom":
            print("You look for your phone in the Bathroom & you finally find it!")
            print("Congrats, you found your phone & your adventure ends here!")
    elif choice2 == "Bathroom":
        print("You look for your phone in the Bathroom & you finally find it!")
        print("Congrats, you found your phone & your adventure ends here!")
    else:
        print("Invalid Command, Try Again...")

elif choice == "Attic":
    print("You look for your phone in the Attic, but you don't find it...")
    choice2 = input("Where will you go now? (Bathroom/Kitchen): ")
    
    if choice2 == "Bathroom":
        print("You look for your phone in the Bathroom & you finally find it!")
        print("Congrats, you found your phone & your adventure ends here!")
    elif choice2 == "Kitchen":
        print("You look for your phone in the Kitchen, but you don't find it...")
        choice3 = input("Where will you go now? (Bathroom): ")
        if choice3 == "Bathroom":
            print("You look for your phone in the Bathroom & you finally find it!")
            print("Congrats, you found your phone & your adventure ends here!")
    else:
        print("Invalid Command, Try Again")

else:
    print("Invalid Command, Try Again")
