########################################
### MY FUNCTIONS AND OTHER VARIABLES ###
########################################
while True:

    gemCount = []
    character_options = [0]*3

    def C_M():
        print("\033[0;32mrecall what you look like...\033[0;0m")
        while True:

            print("NAME")
            print("HEIGHT")
            print("HAIR")
            print("SAVE\n")

            characterMenu = input()
            if characterMenu == ("name"):
                character_options[0] = input("ENTER YOUR NAME\n")
            elif characterMenu == ("height"):
                print("PICK A HEIGHT 1-7\n")
                character_options[1] = int(input())
            elif characterMenu == ("hair"):
                print("PICK A HAIR COLOR BLONDE/BROWN/BLACK")
                character_options[2] = input("BLONDE/BROWN/BLACK\n")
            elif characterMenu == ("save"):
                break
            else:
                print("Please select one of the options.")
    
    def bakery():
        print("\033[0;32mYou take the path leading to the town. Upon entering you smell a delicious pie from the bakery and dedice to check it out.\033[0;0m")
        print(". . .")
        print(f"\033[0;32mHello {character_options[0]}! How are you on this fine T-- Wait. What day is it again? popday, retday, hifday? Help me out here!\033[0;0m\n")
        while True:
            userDay = input()
            dayA = userDay.count("d")
            dayB = userDay.count("a")
            dayC = userDay.count("y")
            dayD = len(userDay)
            if dayA + dayB + dayC >= 3 and dayD ==6:
                print(f"\033[0;32mOh yes, How could I forget it was {userDay}! As thanks, please take this pie!\033[0;0m")
                print("\033[0;32mAs you eat the yummy apple pie, you notice a twinkle. There was a Gem baked inside!\033[0;0m")
                gemCount.append(1)
                print(f"\033[0;32mYou have \033[0;36m{sum(gemCount)} Gem(s)!\033[0;0m")
                print("\033[0;32mI should go back and check the forest...\n\033[0;0m")
                break
            else:
                print("\033[0;32mNo... that doesnt sound right. Something with 6 letters I think?\033[0;0m\n")

    def theForest():
        print("\033[0;32myou make your way through the forest when your met with a Large Ruin. You notice a scale sitting at the entrance. The left has a rock, the right nothing.\033[0;0m")
        print("\033[0;32mYou look nearby and find some pebbles, which side do you want to add too\033[0;0m?")
        leftS = 3
        rightS = 0
        pebble = 1
        while True:
            print("LEFT")
            print("RIGHT\n")
            scaleS = input()
            if scaleS == "left":
                print("You think to yourself you should try the other side")
            elif scaleS == "right":
                rightS += pebble
            else:
                print("Please select an option")
            
            if leftS != rightS:
                print("\033[0;32mI think it needs some more\033[0;0m")
            elif leftS == rightS:
                print("\033[0;32mThe scale balances out and a large stone door quakes open.\033[0;0m")
                break
        if character_options[1] <3:
            print("\033[0;32myou notice a twinkle from a small hole, you seem just small enough to fit!\033[0;0m")
            gemCount.append(1)
            print(f"\033[0;32mYou have \033[0;36m{sum(gemCount)} Gem(s)!\033[0;0m")
        print("\033[0;32mYou enter the ruins and you hear a thundering voice\033[0;0m")
        print("\033[0;32mWhat would you rather have?\033[0;0m")
        print("MONEY")
        print("FAMILY\n")
        greed = 0
        q1 = input()
        if q1 == "money":
            greed += 1
        elif q1 == "family":
            greed += 0
        else:
            print("Please select an option.")

        print("\033[0;32mDo you share your favorite meal with a starving enemy?\033[0;0m")
        print("NO")
        print("YES\n")
        q2 = input()
        if q2 == "no":
            greed += 1
        elif q2 == "yes":
            greed += 0
        else:
            print("Please select an option.")

        if greed == 2 or greed > 2:
            print("\033[0;32mThe door shuts behind you. You stare at a small boy with blonde hair, similar in build to you. He's gone crazy obssessing with over \033[0;36mGems.\033[0;0m")
            print("Y\033[0;32mou sitdown next to him and take out your \033[0;36mGems as well.. staring blankly at them\033[0;0m")
            print(f"\033[0;32mYou got the THE OBBSESSED ENDING, you found \033[0;36m{sum(gemCount)}/3 Gems.\033[0;0m")
        elif greed < 2:
            print("\033[0;32mThe thundering voice asks for your gems, and you pour them into a newly opened hole just big enough to fit them.\033[0;0m")
            print("\033[0;32mLeave. Dont come back here.\033[0;0m")
            print("\033[0;32mYou leave the ruins and think to yourself, I should see my family.\033[0;0m")
#####################################
### THIS IS WHERE THE GAME STARTS ###
#####################################
    print("\033[0;32mW E L C O M E   T O   T H E   R U I N E D\033[0;0m")
    print("PLAY")
    print("EXIT\n")
    menuOptions = input()

    if menuOptions == "play":
        while True:

            print("\033[0;32mYou wake up in a small cottage, little light is coming inside and you notice a mirror, and a painting.\033[0;0m")
            print("1. Interact with the mirror")
            print("2. Interact with the painting")
            print("3. Keep looking around\n")

            cottageOptions = input()

            if cottageOptions == "1":
                C_M()
            elif cottageOptions == "2":
                print("\033[0;32mYou notice it's a painting of a small boy, similar in build to you. He has blonde hair and a somber smile.\033[0;0m")
                print("\033[0;32mAfter inspecting the painting you decide to look into the mirror.\033[0;0m")
                C_M()

            elif cottageOptions == "3":
                print("\033[0;32mYou notice a glimmer in the corner of the room. After wiping away some dust you notice a Gem.\033[0;0m")
                gemCount.append(1)
                print(f"\033[0;32mYou have \033[0;36m{sum(gemCount)} Gem(s)!\033[0;0m")
                print("\033[0;32mAfter finding the gem you decide to look into the mirror.\033[0;0m")
                C_M()
            
            else:
                print("Please select one of the options.")

            print("\033[0;32mAfter gazing into the mirror, you go to the door only to realise its locked. You find a note on a nightstand next to the door saying: \033[0;0m")
            print("\033[0;32mThe first number is the devils mark, the second number can be found in the clouds\033[0;0m")
            while True:
                doorCode = input("ENTER 2-DIGIT LOCK CODE\n")
                if doorCode == "69":
                    print("\033[0;32mit opens!\033[0;0m")
                    break
                else:
                    print("\033[0;32mYou enter the code but it doesnt wiggle.\033[0;0m")

            print("\033[0;32mFinally outside, you walk about 5 feet when you see an old lady approaching on the path.\033[0;0m")
            print("1. Talk to the old lady.")
            print("2. Walk past her.\n")

            gEncounter = input()
            
            if gEncounter == "1":
                if character_options[2] == "blonde":
                    print("\033[0;32mHow did you get out? Come along with me. Its for your own good, Grandma only wants you to be safe...\033[0;0m")
                    print(f"\033[0;32mYou got the LOCKED AWAY ENDING, you found \033[0;36m{sum(gemCount)}/3 Gems!\033[0;0m.\033[0;0m")
                    break
                elif character_options[2] != "blonde":
                    print("\033[0;32mHere, take this shiny rock. My grandson has been obessed with these and its worrying me.\033[0;0m")
                    gemCount.append(1)
                    print(f"You have \033[0;36m{sum(gemCount)} Gem(s)!\033[0;0m")
                else:
                    print("Please select one of the options.")

            if gEncounter == "2":
                print("\033[0;32myou decide to not say anything as you have more important things on your mind.\033[0;0m")
            while True:
                print("\033[0;32mYou continue on your way and are met with a forked road. A sign leads towards a town, the other a forest.\033[0;0m")
                print("\033[0;32mWhere do you want to go?\033[0;0m")
                print("1. THE TOWN")
                print("2. THE FOREST\n")

                roadA = input()

                if roadA == "1":
                    bakery()
                    theForest()
                    break
                elif roadA == "2":
                    theForest()
                    break
                break
            break
                

