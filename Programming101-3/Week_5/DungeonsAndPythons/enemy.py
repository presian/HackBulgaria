from man import Man


class Enemy(Man):

    def __init__(self, health=100, mana=100, damage=20):
        Man.__init__(self, health, mana)
        self.__damage = damage

        def attack(self):
            return self.__damage
