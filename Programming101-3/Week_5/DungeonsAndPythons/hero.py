from man import Man


class Hero(Man):

    def __init__(self, health, mana, name="Baron", title="Dragonslayer", mana_regeneration_rate=2):
        Man.__init__(health, mana)
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.__name = name
        self.__title = title
        self.__weapon = None
        self.__spell = None

    def known_as(self):
        message = "{} {}"
        return message.format(self.name, self.title)

    def take_damage(self, damage_points):
        self.__health -= damage_points

    def has_weapon(self):
        return self.equipped_weapon

    def equip(self, weapon):
        self.__weapon = weapon

    def learn(self, spell):
        self.__spell = spell

    def attack(self, by=None):
        if by == "weapon":
            return self.weapon.get_weapon_damage()
        if by == "magic":
            return self.__spell.get_spell_damage()
        return 0
