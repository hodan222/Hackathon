import operator
from Fight import Fight
from time import sleep
from Player import Player

class Interview():

    candidates = []

    def __init__(self, file_path):
        if file_path == '' or file_path == None:
            raise Exception('Give me the file!!!')
        for line in open(file_path, 'rb'):
            if line.startswith('Name'):
                attr_names = line.strip().split(',')
            elif line:
                self.candidates.append(dict(zip(attr_names,line.strip().split(','))))

    def start(self):
        old_players = {} # an string-Player dict
        result = {}
        for row in self.candidates:
            new_player = Player(row['Name'], int(row['Health']), int(row['Damage']), int(row['Attacks']))
            for pname in old_players:
                f = Fight(old_players[pname], new_player)
                winner = f.fight()
                print '\n##########################################\n'
                # sleep(1)
                if result.has_key(winner):
                    result[winner] += 1
                else:
                    result[winner] = 1
            # add new player to the old player list
            old_players[row['Name']] = new_player
        result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
        print 'Number of winnings: '+str(result)
        print 'Final winner is '+result[0][0]

if __name__ == '__main__':
    iv = Interview('./applicants.csv')
    iv.start()
