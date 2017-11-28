from sys import exit

def start ():
    print "You are in a dark room."
    print "In front of you, there's a table with two cups on it"
    print "Each cup is placed on a button, that will open a door when you drink."
    print "In cup 1 there's water and in cup 2 is vodka"
    print "So, do you drink 1 or 2?"


    choice = raw_input("> ")

    if choice == "1":
        dead ("Water? Really? Go home. Please.")

    elif choice == "2":
        room_bored()


def room_bored():
    print "So we've got a little vodkaholic here, interesting.\nI hope you're not too drunk yet!"
    print "On a scale from 1 to 5, how bored are you from this game?"

    choice = raw_input("> ")
    if "1" in choice or "2" in choice or "3" in choice or "4" in choice or "5" in choice:
        how_much = int(choice)
    else:
        dead ("Well...and I thought I was retarded")

    if how_much >= 3:
        print "Ohhh okay you're that kind of adventurous person?\nCan't stand those people..."
        print "You ask for more action? You will get more action! Any regrets already?"
        room_adventure()

    elif how_much <= 2:
        print "You're NOT bored? Whats wrong with you?"
        room_meeting()


def room_meeting():
    print "Since you like boring stuff, we could do a little small talk session."


    age = raw_input("The most interesting question first: How old are you? ")
    choice = raw_input("> ")

    how_old = int(choice)

    if how_old >=18:
        print "Good, with %r you're old enough for this situation" % (age)
    else:
        print "Ooops %r is too young for this game. You're out" % (age)
        exit(0)

    name = raw_input("Ups, probably should have ask this first, what's your name? ")
    drink = raw_input("Okay and what's your favourite drink? ")
    school = raw_input("Aha aha...favourite subject in school? ")
    food = raw_input("Interesting. Is there any food you don't like? ")
    film = raw_input("On a lonely friday night, what film would you watch? ")

    print "Alright let me check. You like drinking %r, your favourite subject in school is %r and you don't like %r?" %(drink, school, food)
    print "Who wouldn't like %r?" %(food)
    print "And the fact that you're spending friday nights at home watching %r doesn't make it better" %(film)
    print "That doesn't look good %r.\nDoesn't look good." %(name)

    print "I'll give you one last chance.\nDo you like cats yes or no?"

    choice = raw_input("> ")
    if "yes" in choice:
        print "Congrats, you're a cat person! You may go on now."
        room_adventure()
    else:
        print "I won't comment on that %r. You're out" % (name)
        exit (0) #Actually I wanted to do the "dead" statement, but then ne "%"-command doesn't work. So i used exit



def room_adventure():
    print "Are you ready for some action?"
    choice = raw_input("> ")

    if "no" in choice:
        print "You suck. Maybe some alcohol could help."
        print "I've got 5 vodka shots.\nHow many do you want?"

        choice = raw_input("> ")
        how_many = int (choice)

        if how_many <=2:
            dead ("Not impressive.")
        elif how_many >2:
            dead ("Ahh I tricked you there. No more shots for you!")

    else:
        print "Alright let's do this!"
        print "You're on your way home on a foggy monday night."
        print "Suddenly you hear a noise."
        print "You turn around and see Pennywise the Dancing Clown a few steps away."
        print "Your only weapons: A stone, a peanut, your pokeball and a mirror."
        print "What do you use?"




        choice = raw_input("> ")

        if choice == "stone":
            dead ("You just made him mad and he kills you.")
        elif choice == "peanut" :
            dead ("He throws the peanut back at you.\nForgot about your allergy?? You're dead.")
        elif choice == "pokeball":
            dead ("Your pokeball was useless!")

        elif choice == "mirror":
            print "He sees his not matching socks, feels ashamed and runs away.\nLucky you!"
            last_room()
        else:
            print "I have no idea what this means."

def last_room():
    print "You're alive, that's great!"
    print "Let's get a little creative here. Finish the poem and you finish this 'game' or whatever you want to call it."

    poem= """
    \tRoses are red."
    \tSo is wine."
    \tAnd tomato sauce."
    \tThat goes on ?"
    """
    print "-----------------"
    print poem

    choice = raw_input("> ")
    if choice == "pizza":
        print "You have a good taste! Now go out and do other things than just sitting in front of your computer. That's sad."
        exit (0)
    elif choice == "spaghetti":
        print "Eat the spaghetti to forgetti your regretti. No do something with your friends."
    elif choice == "fries":
        print "Not my first choice, but well...Now go get some awesome food and turn on Netflix."
    else:
        dead ("You're not a gourmet. Try again")
        start ()


def dead(why):
    print why, "You're out."
    exit(0)

start ()
