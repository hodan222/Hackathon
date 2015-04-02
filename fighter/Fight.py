from Player import *
from random import random

class Fight():

    def __init__(pa, pb):
        self.__player_a = pa
        self.__player_b = pb

    
    def fight():
        name_a = self.__player_a.get_name()
        damage_a = self.__player_a.get_damage()
        attacks_a = self.__player_a.get_attacks()
        health_a = self.__player_a.get_health()

        name_b = self.__player_b.get_name()
        damage_b = self.__player_b.get_damage()
        attacks_b = self.__player_b.get_attacks()
        health_b = self.__player_b.get_health()

        def show_players():
            # print players' attributes
            print name_a
            print '\tHealth: '+str(health_a)
            print '\tDamage: '+str(damage_a)
            print '\tAttack: '+str(attack_a)
            print '\n'
            print name_b
            print '\tHealth: '+str(health_b)
            print '\tDamage: '+str(damage_b)
            print '\tAttack: '+str(attack_b)


        def go_round(round_=1):
            # fight for a round
            print 'Round: '+str(round_)

            # initiative roll
            rand_a = int(random()*100)
            rand_b = int(random()*100)
            if rand_a < rand_b # a attcks b
                init_stream = name_a' is randomly selected to go first ('+str(rand_a)+' > '+str(rand_b)+')'
            else:
                rand_b += 1 # in case rand_a == rand_b
                init_stream = name_b' is randomly selected to go first ('+str(rand_b)+' > '+str(rand_b)+')'
            print init_stream

            


