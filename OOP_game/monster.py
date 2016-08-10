import random

from combat import Combat

COLORS = ['yellow', 'red', 'blue', 'green', 'purple']


class Monster(Combat):

#create defaults to add to when creating subclasses
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'


#"dunder" init = __init__ sets rules for each spawn of instance
    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key , value in kwargs.items():
            setattr(self, key, value)

#"dunder" str = __str__ = controls how the object is printed

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),
                                              self.__class__.__name__,
                                              self.hit_points,
                                              self.experience)

#need to create and instance before calling methods
#cannot work on Monster.battlecry() because cannot work on the class itself

    def battlecry(self):
        return self.sound.upper()


#creating subclasses that inherit the Monster class and add individual attributes
class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = 'squeak'


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = 'growl'


class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'raaaaaawr'
