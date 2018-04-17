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

    def play(self):
        print("%s is not human" % self.name)


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

    def beat(self):
        print("You slap your chest and your armor makes a hearty pound.")


class Cosmetic(Equipable):
    def __init__(self, name, location, value, look):
        super(Cosmetic, self).__init__(name, location, value)
        self.look = look

    def wear(self):
        print("Your dumb wearing %s" % self.name)


class Material(Item):
    def __init__(self, name, location, value, material):
        super(Material, self).__init__(name, location, value)
        self.material = material

    def feel(self):
        print("Your weird")


# Materials
class Bone(Material):
    def __init__(self, name, location, value, material):
        super(Bone, self).__init__(name, location, value, material)

    def look(self):
        print("It looks decayed")


class Blood(Material):
    def __init__(self, name, location, value, material):
        super(Blood, self).__init__(name, location, value, material)

    def taste(self):
        print("It taste irony")


class Scales(Material):
    def __init__(self, name, location, value, material):
        super(Scales, self).__init__(name, location, value, material)

    def tap(self):
        print("It gives a nice 'thud'")


class Steel(Material):
    def __init__(self, name, location, value, material):
        super(Steel, self).__init__(name, location, value, material)

    def polish(self):
        print("It's shiny again")


class Wood(Material):
    def __init__(self, name, location, value, material):
        super(Wood, self).__init__(name, location, value, material)

    def chip(self):
        print("Why would you break off a piece of armor")


# Weapons
class Sword(Weapon):
    def __init__(self, name, description, location, damage, value):
        super(Sword, self).__init__(name, description, location, damage, value)

    def admire(self):
        print("%s is really broad")


class Club(Weapon):
    def __init__(self, name, description, location, damage, value):
        super(Club, self).__init__(name, description, location, damage, value)

    def swing(self):
        print("Its heavy")


class Sai(Weapon):
    def __init__(self):
        super(Sai, self).__init__("Sai", "Its pointy", 'lair', 15, 2000)

    def spin(self):
        print("It spins along your hands")


class RustyDagger(Weapon):
    def __init__(self, name, description, location, damage, value):
        super(RustyDagger, self).__init__(name, description, location, damage, value)

    def throw(self):
        print("You throw the brown blade")


class NunChuck(Weapon):
    def __init__(self):
        super(NunChuck, self).__init__("Nun-chuck", "It spins", 'lair', 10, 25000)

    def flick(self):
        print("It flicks and is caught in your armpit")


class BoStaff(Weapon):
    def __init__(self):
        super(BoStaff, self).__init__("Bo Staff", "Its a long stick", 'lair', 20, 10)

    def twist(self):
        print("You spin it around your body")


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__("Stick", "It's a stick", 'room', 25, 0)

    def twiddle(self):
        print("You twiddle it between your fingers")


class MelonBratch(Weapon):
    def __init__(self):
        super(MelonBratch, self).__init__("Melon Bratch", "It talks", 'empty_room', 9999999999999999, 99999999999999999)

    def turn_on(self):
        print("It turns on an begins to play 'Smooth Criminal")


# Consumables

class SmallHealthPotion(Consumable):
    def __init__(self):
        super(SmallHealthPotion, self).__init__("Small Health Potion", 'steel_mill''empty_room''vault''sanctuary',
                                                'heal', 200)

    def sip(self):
        print("Taste like cherry")


class LargeHealthPotion(Consumable):
    def __init__(self):
        super(LargeHealthPotion, self).__init__("Small Health Potion", 'steel_mill''sanctuary''sewer_maintenance'
                                                                       'well_lit_room''lair', 'heal', 2000)

    def gulp(self):
        print("You take a fat gulp")


class SmallStaminaPotion(Consumable):
    def __init__(self):
        super(SmallStaminaPotion, self).__init__("Small Stamina Potion", 'steel_mill''empty_room''vault''sanctuary',
                                                 'recover', 200)

    def drink(self):
        print("You drink the yellow liquid")


class LargeStaminaPotion(Consumable):
    def __init__(self):
        super(LargeStaminaPotion, self).__init__("Small Health Potion", 'steel_mill''sanctuary''sewer_maintenance'
                                                                        'well_lit_room''lair', 'heal', 2000)

    def swig(self):
        print("Your take a fat swig of the potion")


# Cosmetics

class Binky(Cosmetic):
    def __init__(self):
        super(Binky, self).__init__("Binky", 'echoing_room', 100000, "In your mouth")

    def cry(self):
        print("Aww is the little baby crying")


class Bonnet(Cosmetic):
    def __init__(self):
        super(Bonnet, self).__init__("Bonnet", 'lego_room', 100000, "On your head")

    def sit(self):
        print("You plop yourself down and begin to suck your thumb")


class ChickenHat(Cosmetic):
    def __init__(self):
        super(ChickenHat, self).__init__("Chicken Hat", 'final_boss_room', 20, "You look dumb")

    def dance(self):
        print("Your an even bigger joke now")


class TrackSuit(Cosmetic):
    def __init__(self):
        super(TrackSuit, self).__init__("Adidas Track Suit", 'room', 20, "You look like a man now.")

    def squat(self):
        print("You squat")


class WinterCoat(Cosmetic):
    def __init__(self):
        super(WinterCoat, self).__init__("Winter Coat", 'hot_room', 20, "You're no longer hot.")

    def rap(self):
        print("Mans not hot")


# Armor

class Boots(Armor):
    def __init__(self, name, location, value, defense):
        super(Boots, self).__init__(name, location, value, defense)

    def kick(self):
        print("You kick the air")


class Helmet(Armor):
    def __init__(self, name, location, value, defense):
        super(Helmet, self).__init__(name, location, value, defense)

    def headbutt(self):
        print("You headbutt the air")


class Breastplate(Armor):
    def __init__(self, name, location, value, defense):
        super(Breastplate, self).__init__(name, location, value, defense)

    def chestbump(self):
        print("You chest bump the air")


class Leggings(Armor):
    def __init__(self, name, location, value, defense):
        super(Leggings, self).__init__(name, location, value, defense)

    def lunge(self):
        print("You begin to lunge\n"
              "Can't forget leg day")


legs = Leggings("Legs", 'you', 0, 0)
legs.lunge()

head = Helmet("Head", 'you', 0, 0)
head.headbutt()
