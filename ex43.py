from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):
  
    def enter(self):
        print("this scene is not yet configured!")
        print("Subclass it and implement enter().")
        exit(1)
  

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print(f"current scene={current_scene}")
        last_scene = self.scene_map.next_scene('finished')
        print(f"last_scene={last_scene}")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            print(f"next_scene_name={next_scene_name}")
            current_scene = self.scene_map.next_scene(next_scene_name)
            print(f"current scene={current_scene}")
     
class Death(Scene):

    def enter(self):    
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        return 'laser_weapon_armory' 

class LaserWeaponArmory(Scene):

    def enter(self):
        return 'the_bridge' 

class TheBridge(Scene):

    def enter(self):
        return 'escape_pod'

class EscapePod(Scene):

    def enter(self):
        return 'finished' 


class Finished(Scene):
   
    def enter(self):
        print('You won! Good job.')
        return 'finished' 

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


