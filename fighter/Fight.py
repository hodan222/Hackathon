from Player import Player
from time import sleep
import copy
from random import random

class Fight():

    def __init__(self, pa, pb):
        self.__player_a = pa
        self.__player_b = pb

    def set_player_a(self, pa):
        self.__player_a = pa

    def set_player_b(self, pb):
        self.__player_b = pb

    def get_player_a(self):
        return self.__player_a

    def get_player_b(self):
        return self.__player_b

    def fight(self):
        # make copies for original players
        pac = copy.deepcopy(self.__player_a)
        pbc = copy.deepcopy(self.__player_b)

        # functions to show players attributes
        def show_players():
            # print players' attributes
            print '\n'
            print pac.get_name()
            print '\tHealth: '+str(pac.get_health())
            print '\tDamage: '+str(pac.get_damage())
            print '\tAttack: '+str(pac.get_attacks())
            print '\n'
            print pbc.get_name()
            print '\tHealth: '+str(pbc.get_health())
            print '\tDamage: '+str(pbc.get_damage())
            print '\tAttack: '+str(pbc.get_attacks())
            return 

        # functions for fighting a round
        def go_round(round_=1):
            # fight for a round
            print 'Round: '+str(round_)
            current_attacker = 'a'

            # initiative roll
            rand_a = int(random()*100)
            rand_b = int(random()*100)
            if rand_a > rand_b: # a attcks b first
                current_attacker = 'a'
                init_stream = '\t'+pac.get_name()+' is randomly selected to go first ('+str(rand_a)+' > '+str(rand_b)+')'
            else:
                current_attacker = 'b'
                rand_b += 1 # in case rand_a == rand_b
                init_stream = '\t'+pbc.get_name()+' is randomly selected to go first ('+str(rand_b)+' > '+str(rand_a)+')'
            print init_stream

            # start fighting !
            pac.set_attacks(self.__player_a.get_attacks())
            pbc.set_attacks(self.__player_b.get_attacks())
            while pac.get_attacks() > 0 or pbc.get_attacks() > 0: # one of two players have attacks
                if current_attacker == 'a':
                    have_winner, winner_name = deal_an_attack(pac, pbc)
                    if have_winner:
                        return True, winner_name
                    elif pbc.get_attacks() > 0: # player B have attacks remain
                        current_attacker = 'b'
                elif current_attacker == 'b':
                    have_winner, winner_name = deal_an_attack(pbc, pac)
                    if have_winner:
                        return True, winner_name
                    elif pac.get_attacks() > 0: # player B have attacks remain
                        current_attacker = 'a'
            # both have health
            return False, None

        # function for an attack in a round
        # return True if taget is dead
        def deal_an_attack(attacker, target):
            attacker.set_attacks( attacker.get_attacks() - 1 )
            dmg = attacker.get_damage()
            health1 = target.get_health()
            health2 = health1 - dmg
            target.set_health(health2)
            print '\t'+attacker.get_name()+' hits '+target.get_name()+' for '+str(dmg)+' damage ('+str(health1)+' -> '+str(health2)+')'
            if health2 <= 0:
                print '\t'+attacker.get_name()+' wins!'
                return True, attacker.get_name()
            return False, None


        # Main part for fight()
        show_players()
        print '\n'
        sleep(1)
        is_over = False
        r = 1
        while not is_over:
            is_over, winner = go_round(round_=r)
            print '\n'
            sleep(1)
            r += 1
        return winner


# For Test
if __name__ == '__main__':
    pa = Player('Haodan', 99, 9, 2)
    pb = Player('SB', 50,1,5)
    f = Fight(pa, pb)
    print f.fight()


