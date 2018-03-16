class Item(object):
    def __init__(self, name, location, value=0):
        self.name = name
        self.location = location
        self.value = value

    def take(self):
        print("You take %s" % self.name)

    def buy(self):
        print("You buy the %s" % self.name)

    def sell(self):
        print("You sell the %s" % self.name)


class Weapon(Item):
    def __init__(self, name, description, location, damage=0, value=0):
        super(Weapon, self).__init__(name, location, value)
        self.description = description
        self.damage = damage


class Consumable(Item):
    def __init__(self, name, location, effect, value=0):
        super(Consumable, self).__init__(name, location, value)
        self.effect = effect

    def use(self):
        print("You use %s" % self.name)


class Equipable(Item):
    def __init__(self, name, location, value):
        super(Equipable, self).__init__(name, location, value)

    def equip(self):
        print("You equip %s" % self.name)


class Armor(Equipable):
    def __init__(self, name, location, value, defense=0):
        super(Armor, self).__init__(name, location, value)
        self.defense = defense


class Cosmetic(Equipable):
    def __init__(self, name, location, value, look):
        super(Cosmetic, self).__init__(name, location, value)
        self.look = look


class Material(Item):
    def __init__(self, name, location, value, material):
        super(Material, self).__init__(name, location, value)
        self.material = material


# Materials
class Bone(Material):
    def __init__(self, name, location, value, material):
        super(Bone, self).__init__(name, location, value, material)


class Blood(Material):
    def __init__(self, name, location, value, material):
        super(Blood, self).__init__(name, location, value, material)


class Scales(Material):
    def __init__(self, name, location, value, material):
        super(Scales, self).__init__(name, location, value, material)


class Steel(Material):
    def __init__(self, name, location, value, material):
        super(Steel, self).__init__(name, location, value, material)


class Wood(Material):
    def __init__(self, name, location, value, material):
        super(Wood, self).__init__(name, location, value, material)


# Weapons
class Club(Weapon):
    def __init__(self, name, location, value, description, damage):
        super(Club, self).__init__(name, location, value, description, damage)


class