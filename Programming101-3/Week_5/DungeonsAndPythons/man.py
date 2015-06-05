class Man:

    HEALTH_MIN = 0
    HEALTH_MAX = 100
    MANA_MIN = 0
    MANA_MAX = 100

    def __init__(self, health=100, mana=100):
        self.__health = health
        self.__mana = mana

    def is_alive(self):
        return self.__health > Man.HEALTH_MIN

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def can_cast(self):
        return self.mana > Man.MANA_MIN

    def take_mana(self, mana_points):
        if self.__mana + mana_points >= Man.MANA_MAX:
            self.__mana = Man.MANA_MAX
        else:
            self.__mana += mana_points

    def take_healing(self, healing_points):
        if self.__health + healing_points >= Man.HEALTH_MAX:
            self.__health = Man.HEALTH_MAX
        else:
            self.__health += healing_points
