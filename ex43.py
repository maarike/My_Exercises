from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print ”This scene is not yet configured. Subclass it and implement enter().”
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene(’finished’)

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


        current_scene.enter()

class Death(Scene):
    quips = [
    ”You died. You kinda suck at this.”,
    ”Your mom would be proud... she were smarter.”,
    ”Such a luser.”,
    ”Ihaveasmallpuppythat’sbetteratthis.”
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "Your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutrin destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship after getting intor an"
        print "escape pod."


        action = raw_input(>" ")

        if action == "shoot!":
            print "Quick on the drwa you yank out your blaster and fire it at the Gothon."

        elif action == "dodge!":
            print "The Gothon eats you"
            return 'death'

        elif action == "tells a joke":
            print "You win"
            return 'laser_weapon armory'
        else:
            print "Does Not compute"
            return 'central_corridor'
        
