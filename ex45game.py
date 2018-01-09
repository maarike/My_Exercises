from sys import exit
from random import randint


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Scene (object):

    def enter(self):
        print "?"
        exit (1)



class Hoersaalgang (Scene):
    def enter(self):
        print "This morning you decided to go to university."
        print "You regret it immediatly after you've spilled you morning coffee everywhere."
        print "Everyhing you want is going home and watching another Breaking Bad episode."
        print "I mean season."
        print "\n"
        print "In order to go home, you need to go to the bus station."
        print "Right now you're in the Hoersaalgang."
        print "Due to building sites, you can just go LEFT or RIGHT in order to move on."
        print "In which direction do you go?"

        choice = raw_input("> ")
        if choice == "RIGHT":
            return 'studio_21'

        elif choice == "LEFT":
            return 'cafe_9'

        else:
            print "learn how to type."
            return 'hoersaalgang_uni'


class Cafe9(Scene):
    def enter (self):
        print "Welcome to Cafe 9. It's not expensive at all (not)"
        print "You can choose between a COKE and FRANZBROETCHEN."

        choice = raw_input("> ")
        if choice == "COKE":
            print "pretty expensive but you it's worth it."
            return 'studio_21'

        elif choice == "FRANZBROETCHEN":
            print "Bad choice. It's so dry, that it's stuck in your throat."
            print "Next time you should go to Hamburg to eat a franzbroetchen."
            return 'death'

        else:
            print "learn how to type."
            return 'cafe_9'

class Studio21(Scene):
    def enter (self):
        print "Oh deer you end up in the sport studio 21."
        print "Since you didn't do any sports for 4 years, this could be interesting."
        print "Unfortunately a motivated sport student bumbs into you and persuades you to take a cours right away."
        print "You can chose between ZUMBA and BODY PUMP."
        print "Which one do you take?"

        choice = raw_input("> ")
        if choice == "ZUMBA":
            print "A student next to you accidentally punches you in your face while doing an exaggerating dance move"
            print "You are k.o."
            return 'death'

        elif choice == "BODY PUMP":
            print "Risky choice!"
            print "A sport student challenges you to do more sit ups than him."
            print "How many sit ups do you think you can do?"
            print "Be warned! If you lose, you will have to do the entire sport session until the bitter end."
            print "If you win, you can leave whenever you want"


            choice = raw_input("> ")
            how_many = int (choice)

            if how_many <15:
                print "Seriously? That's not really impressive. You lost."
                return 'death'
            else:
                print "Well played, your muscles are crying, but you can get out of this hell."
                print "There is a GREEN and an ORANGE door. Which one do you take? Type in the color."

                choice = raw_input("> ")
                if choice == "ORANGE":
                    print "Alright, you're on your way to the Mensa."
                    return 'mensa_essen'

                elif choice == "GREEN":
                    print "Alright, you're on your way to the Men- "
                    return 'uwi_student'

                else:
                    print "learn how to type."
                    return 'studio_21'

        else:
            print "learn how to type"
            return 'studio_21'


class UwiStudent(Scene):
    def enter (self):
        print "Well shit a wild uwi student appears!"
        print "In his left hand he's got a joint, in his right hand a piece of tofu."
        print "What? I don't know why he's got tofu to go. Uwis are weird."
        print "Are you going to take a drag from the JOINT or a bite from the TOFU?"

        choice = raw_input ("> ")
        if choice == "JOINT":
            print "The uwi student is satisfied. You may go on now."
            return 'mensa_essen'

        elif choice == "TOFU":
            print " The tofu is so dry, that it's stuck in your throat. You die."
            return 'death'

        else:
            print "learn how to type."
            return 'uwi_student'


class Mensa(Scene):
    def enter (self):
        print 'Welcome to the greatest *not* mensa of all time.'
        print "Follwing dishes are on the menue:"

        dishes = "CURRYWURST, FISH, LASAGNE"
        print dishes
        print "Not very tasty I know..."
        print "But now it's your choice. Which one do you take?"

        choice = raw_input("> ")
        if choice == "LASAGNE":
            print "Good choice."
            print "But today the Lasagne is really salty."
            print "You can't afford a bottle of water, because you're broke."#
            print "You can only get to the toilette to drink some water."
            print "Unfortunately both signs for the toilets are ripped off."
            print "So you don't know what's the woman and man bathroom."
            print "Guess. RIGHT or LEFT door?"

            choice = raw_input("> ").upper
            if choice == "right":
                print "You're in the men's toilet. You die of maximum embarrassment."
                return 'death'
            elif choice == "left":
                print "Lucky you! You're in the Lady's toilet. No need to worry."
                return 'bus_station'


        elif choice =="FISH":
            print "#Healthylifestyle! Respekt!"
            print "Sadly you can't get any fries, because they're sold out."
            print "You can chose between COUSCOUS and BAKED POTATOES."

            choice = raw_input("> ")
            if choice == "COUSCOUS":
                print "Seriously? That's disgusting"
                return 'death'
            elif choice == "BAKED POTATOS":
                print "Good choice!"
                print "You finished your meal and can go on now."
                return 'bus_station'
            else:
                print "learn how to type."
                return 'mensa_essen'


        elif choice == "CURRYWURST":
            print "Good choice!"
            print "The only food you can really count on."
            print "You're enjoying your meal and go on to the last level."
            return 'bus_station'
        else:
            print "learn how to type."
            return 'mensa_essen'


class Bus(Scene):
    def enter (self):
        print "Congrats you made it out of university!"
        print "Soon you'll be home "
        print "You can take the 5011 or 5012"
        print "Whoch one will you take?"

        choice = raw_input ("> ")
        if choice == "5011":
            print "You step into the bus."
            print "You realize, that you forgot your semesterticket."
            print "When you guess the right code, you can take the ride for free."
            code = "%d%d%d" % (randint (1,5), randint (1,5), randint (1,5))
            guess = raw_input("[keypad]> ")
            guesses = 0


            while guess != code and guesses <6:
                print "I'm waiting."
                guesses =+ 1
                guess = raw_input("[keypad]> ")

            if guess == code:
                print "Congrats! You're on your way home."
                return 'finished'
        elif choice == "5012":
            print "This bus is not coming."#
            print "You don't reach your destiny"
            return 'death'


class Death(Scene):
    quips = [
    "You're not made for university, sorry."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Finished(Scene):
    def enter (self):
        print "You successfully sneaked out of university."
        print "You're a really good student"
        print "Now you can be lazy."



class Map (object):

    scenes ={
    'hoersaalgang_uni': Hoersaalgang(),
    'cafe_9': Cafe9(),
    'studio_21': Studio21(),
    'uwi_student': UwiStudent(),
    'mensa_essen': Mensa(),
    'bus_station': Bus(),
    'death': Death(),
    'finished': Finished(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene (self):
        return self.next_scene(self.start_scene)

a_map = Map ('hoersaalgang_uni')
a_game = Engine(a_map)
a_game.play()
