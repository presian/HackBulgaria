from weapon import Weapon


class Spell(Weapon):

    def __init__(self, name, damage, mana_cost, cast_range):
        Weapon.__init__(self, name, damage)
        self.__mana_cost = mana_cost
        self.__cast_range = cast_range

    def get_spell_name(self):
        return self.__name

    def get_spell_damage(self):
        return self.__damage

    def get_spell_mana_cost(self):
        return self.__mana_cost

    def get_cast_range(self):
        return self.__cast_range
