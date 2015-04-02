
class Player():

    def __init__(name,health,damage,attacks,dodge=0,critical=0,initiative=0):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__attacks = attacks
        self.__dodge = dodge
        self.__critical = critical
        self.__initiative = initiative


    def set_name(name):
        self.__name = name

    def set_health(health):
        self.__health = health

    def set_attacks(attacks):
        self.__attacks = attacks

    def set_dodge(dodge):
        self.__dodge = dodge

    def set_critical(critical):
        self.__critical = critical

    def set_initiative(initiative):
        self.__initiative = initiative


    def get_name(name):
        return self.__name

    def get_health(health):
        return self.__health

    def get_attacks(attacks):
        return self.__attacks

    def get_dodge(dodge):
        return self.__dodge

    def get_critical(critical):
        return self.__critical

    def get_initiative(initiative):
        return self.__initiative
