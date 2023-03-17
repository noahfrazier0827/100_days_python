
while True:

    gemCount = 0
    pName = 0
    pHeight = 0
    pHaircolor = 0

    def C_M():
        print("recall what you look like...")
        while True:

            global pName
            global pHeight
            global pHaircolor

            print("NAME")
            print("HEIGHT")
            print("HAIR")
            print("SAVE")

            characterMenu = input()

            if characterMenu == ("name"):
                pName = input("ENTER YOUR NAME")
            elif characterMenu == ("height"):
                pHeight = input("PICK A HEIGHT 1-7")
            elif characterMenu == ("hair"):
                print("PICK A HAIR COLOR BLONDE/BROWN/BLACK")
                pHaircolor = input("BLONDE/BROWN/BLACK")
            elif characterMenu == ("save"):
                break
            else:
                print("Please select one of the options.")

    print("W E L C O M E   T O   T H E   R U I N E D")
    print("PLAY")
    print("EXIT\n")

    menuOptions = input()

    if menuOptions == "play":
        while True:

            print("You wake up in a small cottage, little light is coming inside and you notice a mirror, and a painting.")
            print("1. Interact with the mirror")
            print("2. Interact with the painting")
            print("3. Keep looking around")

            cottageOptions = input()

            if cottageOptions == "1":
                C_M()
            elif cottageOptions == "2":
                print("You notice it's a painting of asmall boy, similar in build to you. He has blonde hair and a somber smile.")
                print("After inspecting the painting you decide to look into the mirror.")
                C_M()

            elif cottageOptions == "3":
                print("You notice a glimmer in the corner of the room. After wiping away some dust you notice a Gem.")
                gemCount += 1
                print(f"You have {gemCount} Gem(s)!")
                print("After finding the gem you decide to look into the mirror.")
                C_M()
            
            else:
                print("Please select one of the options.")

            print("After gazing into the mirror, you go to the door only to realise its locked. You find a note on a nightstand next to the door saying: ")
            print("The first number is the devils mark, the second number can be found in the clouds")
            while True:
                doorCode = input("ENTER 2-DIGIT LOCK CODE")
                if doorCode == "69":
                    print("it opens!")
                    break
                else:
                    print("You enter the code but it doesnt wiggle.")

            print("Finally outside, you walk about 5 feet when you see an old lady approaching on the path.")
            print("1. Talk to the old lady.")
            print("2. Walk past her.")
            print(pHaircolor)

            gEncounter = input()
            
            if gEncounter == "1":
                print("Oh hello dear...")
                if pHaircolor == "blonde":
                    print("How did you get out? Come along with me. Its for your own good, Grandma only wants you to be safe...")
                    print("LOCKED AWAY ENDING")
                    break
                elif pHaircolor is not "blonde":
                    print("Here, take this shiny rock. My grandson has been obessed with these and its worrying me.")
                    gemCount += 1
                    print(f"You have {gemCount} Gem(s)!")
                else:
                    print("Please select one of the options.")

                

