
class Player():

    def __init__(self, name,health,damage,attacks,dodge=0,critical=0,initiative=0):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__attacks = attacks
        self.__dodge = dodge
        self.__critical = critical
        self.__initiative = initiative


    def set_name(self, name):
        self.__name = name

    def set_health(self, health):
        self.__health = health

    def set_attacks(self, attacks):
        self.__attacks = attacks

    def set_damage(self, damage):
        self.__damage = damage

    def set_dodge(self, dodge):
        self.__dodge = dodge

    def set_critical(self, critical):
        self.__critical = critical

    def set_initiative(self, initiative):
        self.__initiative = initiative


    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_attacks(self):
        return self.__attacks

    def get_damage(self):
        return self.__damage

    def get_dodge(self):
        return self.__dodge

    def get_critical(self):
        return self.__critical

    def get_initiative(self):
        return self.__initiative

    def to_string(self):
        return self.__name
