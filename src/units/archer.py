from unit import Unit

class Archer(Unit):
    def __init__(self, _class, _hp, _armor, _mresist, _damage, _speed, _x, _y):
        super().__init__(_class, _hp, _armor, _mresist, _damage, _speed, _x, _y)

    def do_range_damage(self, enemy): # needs range and los checks
        atk = self._damage
        defence = enemy._armor
        if atk > defence:
            damage = atk - defence
            enemy._hp -= damage