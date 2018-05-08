import random


print("Welcome to Zurk the dumbest game you'll ever play!\n")


class Item(object):
    def __init__(self, name, location, value=0):
        self.name = name
        self.location = location
        self.value = value

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


class Equippable(Item):
    def __init__(self, name, location, value):
        super(Equippable, self).__init__(name, location, value)

    def equip(self):
        print("You equip %s" % self.name)
        global current_item


class Armor(Equippable):
    def __init__(self, name, location, value, defense=0, material=None):
        super(Armor, self).__init__(name, location, value)
        self.defense = defense
        self.material = material


class Cosmetic(Equippable):
    def __init__(self, name, location, value, look):
        super(Cosmetic, self).__init__(name, location, value)
        self.look = look

    def wear(self):
        print("Your dumb wearing %s" % self.name)


class Material(Item):
    def __init__(self, name, location, value, damage_mitigation=0.0):
        super(Material, self).__init__(name, location, value)
        # self.armor_mitigation = character.attack * damage_mitigation


# Materials
class Bone(Material):
    def __init__(self, name, location, value):
        super(Bone, self).__init__(name, location, value, 0.5)


class Blood(Material):
    def __init__(self, name, location, value):
        super(Blood, self).__init__(name, location, value, 0.000001)


class Scales(Material):
    def __init__(self, name, location, value):
        super(Scales, self).__init__(name, location, value, 0.0)


class Steel(Material):
    def __init__(self, name, location, value):
        super(Steel, self).__init__(name, location, value, 0.40)


class Wood(Material):
    def __init__(self, name, location, value):
        super(Wood, self).__init__(name, location, value)


# Weapons
class LightBlade(Weapon):
    def __init__(self):
        super(LightBlade, self).__init__("Light Blade", "It makes a buzzing sound", 'vault', 500, 20000)


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Sword", "Its broad", 'lair', 350, 250)


class Club(Weapon):
    def __init__(self):
        super(Club, self).__init__("Club", "Its big and heavy", 'steel_mill', 500, 200)


class Sai(Weapon):
    def __init__(self):
        super(Sai, self).__init__("Sai", "Its pointy", 'lair', 150, 2000)


class RustyDagger(Weapon):
    def __init__(self):
        super(RustyDagger, self).__init__("Rusty Dagger", "Make sure to get a tetanus shot.", 'lego_room', 1, 0)


class NunChuck(Weapon):
    def __init__(self):
        super(NunChuck, self).__init__("Nun-chuck", "It spins", 'lair', 100, 25000)


class BoStaff(Weapon):
    def __init__(self):
        super(BoStaff, self).__init__("Bo Staff", "Its a long stick", 'lair', 200, 10)


class Stick(Weapon):
    def __init__(self):
        super(Stick, self).__init__("Stick", "It's a stick", 'room', 258, 0)


class MelonBratch(Weapon):
    def __init__(self):
        super(MelonBratch, self).__init__("Melon Bratch", "It talks", 'empty_room', 9999999999999999, 99999999999999999)


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


class Bonnet(Cosmetic):
    def __init__(self):
        super(Bonnet, self).__init__("Bonnet", 'lego_room', 100000, "On your head")


class ChickenHat(Cosmetic):
    def __init__(self):
        super(ChickenHat, self).__init__("Chicken Hat", 'final_boss_room', 20, "You look dumb")


class TrackSuit(Cosmetic):
    def __init__(self):
        super(TrackSuit, self).__init__("Track Suit", 'room', 20, "You look like a man now.")


# Armor

class Boots(Armor):
    def __init__(self, name, location, value, defense, material):
        super(Boots, self).__init__(name, location, value, defense, material)


class Helmet(Armor):
    def __init__(self, name, location, value, defense, material):
        super(Helmet, self).__init__(name, location, value, defense, material)


class Breastplate(Armor):
    def __init__(self, name, location, value, defense, material):
        super(Breastplate, self).__init__(name, location, value, defense, material)


class Leggings(Armor):
    def __init__(self, name, location, value, defense, material):
        super(Leggings, self).__init__(name, location, value, defense, material)


class Character(object):
    def __init__(self, name, race, occupation, mode, status, attack_type, health=100, money=0, target=None, dmg=0,
                 damage_taken=0):
        self.name = name
        self.race = race
        self.occupation = occupation
        self.mode = mode
        self.status = status
        self.attack_type = attack_type
        self.health = health
        self.money = money
        self.target = target
        self.dmg = dmg
        self.damage_taken = dmg
        self.inventory = []

    def take_damage(self, damage_taken):
        self.health -= damage_taken

    def attack(self, target):
        attack_chance = random.randint(1, 6)

        if attack_chance > 1:
            target.take_damage(self.damage_taken)
            print("%s attacks %s." % (self.name, target.name))
            print("It hits.")
            print("%s takes %s damage." % (target.name, self.damage_taken))
        else:
            print("%s misses." % self.name)

        if self.health == 0:
            print(target.name + " has died")
            self.status = 'dead'
        if target.status == 'dead':
            print(target.name + " is already dead")
            return

    def defend(self, me):
        if self.mode in ['hostile', 'neutral']:
            print("You defend.")
            print("You successfully defended yourself.")
        else:
            print("It connects you have been hit")

    def take(self, item):
        self.inventory.append(item)
        print("You take the %s" % item_requested)

    def drop(self, item):
        self.inventory.remove(item)
        print("Dropped")

    def flee(self):
        global current_node
        chosen_direction = random.choice(directions)
        try:
            current_node.move(chosen_direction)
            print("You flee successfully")
            return True
        except KeyError:
            print("You fail to flee")
            return False

    def view_inventory(self):
        try:
            print("There is %s present in the room" % ",".join(list(room.item)))
            return True
        except TypeError:
            print("Nothing is here")
            return False


# Instantiation of items
track_suit = TrackSuit()
chicken_hat = ChickenHat()
bonnet = Bonnet()
binky = Binky()

# Armor Items

# Blood

boots = Boots("Bloody Boots", 'echoing_room', 0, 0, Blood("Blood", None, 0))
helmet = Helmet("Bloody Helmet", 'echoing_room', 0, 100, Blood("Blood", None, 0))
breastplate = Breastplate("Bloody Breastplate", 'echoing_room', 0, 0, Blood("Blood", None, 0))
leggings = Leggings("Bloody Leggings", 'echoing_room', 0, 100,  Blood("Blood", None, 0))

# Steel

boots1 = Boots("Steel Boots", 'room', 100, 20, Steel("Steel", None, 100))
helmet1 = Helmet("Steel Helmet", 'room', 100, 15, Steel("Steel", None, 100))
breastplate1 = Breastplate("Steel Breastplate", 'room', 150, 30, Steel("Steel", None, 100))
leggings1 = Leggings("Steel Leggings", 'room', 100, 20, Steel("Steel", None, 100))

# Bone

boots2 = Boots("Boney Boots", 'sewer_maintenance', 0, 10, Bone("Bone", None, 0))
helmet2 = Helmet("Boney Helmet", 'sewer_maintenance', 0, 10, Bone("Bone", None, 0))
breastplate2 = Breastplate("Boney Boots", 'sewer_maintenance', 0, 10, Bone("Bone", None, 0))
leggings2 = Leggings("Boney Leggings", 'sewer_maintenance', 0, 10, Bone("Bone", None, 0))

# Scales

boots3 = Boots("Scaly Boots", 'vault', 999, 200, Scales("Scale", None, 150))
helmet3 = Helmet("Scaly Boots", 'vault', 999, 150, Scales("Scale", None, 150))
breastplate3 = Breastplate("Scaly Boots", 'vault', 999, 250, Scales("Scale", None, 150))
leggings3 = Leggings("Scaly Boots", 'vault', 999, 150, Scales("Scale", None, 150))

# Wood

boots4 = Boots("Wooden Boots", 'lava_room', 50, 15, Wood("Wood", None, 20))
helmet4 = Helmet("Wooden Helmet", 'lava_room', 50, 10, Wood("Wood", None, 20))
breastplate4 = Breastplate("Wooden Breastplate", 'lava_room', 50, 20, Wood("Wood", None, 20))
leggings4 = Leggings("Wooden Leggings", 'lava_room', 50, 15, Wood("Wood", None, 20))

# Consumables

health_potion = SmallHealthPotion()
bigger_health_potion = LargeHealthPotion()
stamina_potion = SmallStaminaPotion()
bigger_stamina_potion = LargeStaminaPotion()

# Weapons

melon_bratch = MelonBratch()
light_blade = LightBlade()
nun_chuck = NunChuck()
stick = Stick()
bostaff = BoStaff()
rusty_dagger = RustyDagger()
sai = Sai()
club = Club()
sword = Sword()

# Characters

main_character = Character("Dave", 'nugu', 'radish_farmer', 'hostile', 'alive', 'bludgeon', 100, 1000, None, 25)
bar_tender = Character("Matilda", 'human', 'bar_tender', 'friendly', 'alive', None, money=9999999)
bar_patron = Character("Craig", 'elf', 'bum', 'friendly', 'alive', None, 100, 5)
boss1 = Character("Ukifak Lasgoni", 'orc', 'war_lord', 'hostile', 'alive', 'swing', 200000, 0, None, 500)
boss2 = Character("JoJo", 'human', '?', 'hostile', 'alive', 'punch', 1000000, 0, None, 60)
final_boss = Character("Captain Poof Wonder", 'human', 'knight_captain', 'hostile', 'deceased', None)
dio = Character("Dio", 'human', 'annoyance', 'hostile', 'alive', 'swing', 1000, 0, None, 25)
leonarda = Character("Leonarda", 'tortoise', 'ninja', 'neutral', 'alive', 'swipe')
donetella = Character("Donatella", 'tortoise', 'ninja', 'neutral', 'alive', 'swing')
michaelangela = Character("Michaelangela", 'tortoise', 'ninja', 'neutral', 'alive', 'swing')
rophel = Character("Rophel", 'tortoise', 'ninja', 'neutral', 'alive', 'stab')
splinker = Character("Splinker", 'rat', 'unknown', 'friendly', 'alive', None)
hot_mans = Character("Lil' RiceGrain", 'human', 'rapper', 'neutral', 'alive', 'shoot', 2)
dwarf = Character("Harold", 'dwarf', 'theif', 'hostile', 'alive', 'shank')
worshipper1 = Character("Kristofer", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10, 0, None, 10)
worshipper2 = Character("Lonny", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10, 0, None, 10)
worshipper3 = Character("Eliseo", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10, 0, None, 10)
worshipper4 = Character("Ibrahim", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10, 0, None, 10)
worshipper5 = Character("Dante", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10, 0, None, 10)
osian = Character("Katou", 'orange_beast', 'jerk', 'hostile', 'alive', 'swipe', 999999999999999999999999999999999999,
                  0, None, 1)
mj = Character("Michael Jackson", 'human', 'singer', 'hostile', 'alive', 'flick', 10000000, 0, None, 10000000)


class Room(object):
    def __init__(self, name, location, description, north, south, east, west, north_west, north_east, south_east,
                 south_west, characters=None, item=None):
        self.name = name
        self.location = location
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.north_west = north_west
        self.north_east = north_east
        self.south_west = south_west
        self.south_east = south_east
        self.characters = characters
        self.item = item

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


directions = ['north', 'south', 'east', 'west', 'north_west', 'north_east', 'south_east', 'south_west']
short_direction = ['n', 's', 'e', 'w', 'nw', 'ne', 'se', 'sw']

# Initialize Rooms
room = Room("Room", 'room', "You are in a room with a torn up couch and claw marks on a wall.\n"
                            "There is a track suit and a set of steel armor with a sword present.\n"
                            "There is only exits to the South, West and North East.",
            None, 'echoing_room',
            'lego_room', None, None, 'steel_mill', None, None, None, [track_suit, boots1, helmet1, breastplate1,
                                                                      leggings1, sword])
steel_mill = Room("Steel Mill", 'steel_mill', "You enter a room with the Orc Warlord Ukifak Lasgoni.\n"
                                              "You cannot leave to the southeast or west", None, None, None,
                  'empty_room', None, None, 'room', None, [boss1], [health_potion, stamina_potion])
empty_room = Room("Empty Room", 'empty_room', "You enter an empty room all that is there is a button.", None, None,
                  'steel_mill', None, None, None, None, None, [], [melon_bratch, health_potion, stamina_potion])
echoing_room = Room("Echoing Room", 'echoing_room', "You enter an empty room. You feel an annoying presence.", 'room',
                    'sanctuary', None, 'well_lit_room', None, None, None, None, [osian], [boots, helmet, breastplate,
                                                                                          leggings, binky])
well_lit_room = Room("Well Lit Room", 'well_lit_room', "You enter a well lit room with a heavily armored JoJo.\n"
                                                       "He seems aggressive as he mutters 'Omae wa moe shinderu'.",
                     None, None, 'echoing_room', 'vault',
                     None, None, None, None, [boss2], [bigger_health_potion, bigger_stamina_potion])
vault = Room("Vault of Undeniably Valuable Really Long Name Loot", 'vault',
             "You enter a room filled with gold.\n"
             "In the center of the room there is a pedestal.\n"
             "In the pedestal there is a weapon.", None, 'sewer_maintenance', 'well_lit_room', None, None, None, None,
             None, [], [health_potion, stamina_potion, light_blade, boots3, helmet3, breastplate3, leggings3])
sewer_maintenance = Room("Sewer Maintenance", 'sewer_maintenance',
                         "You fall down a hole and break your legs there is no way out.\n"
                         "The room is dark, you feel a hostile presence.", None, None, 'lair',
                         None, None, None, None, None, None, [boots2, helmet2, breastplate2, leggings2])
lair = Room("Lair", 'lair', "The room is dark, there are four shadowy figures who begin to approach you.", None, None,
            None, None, None, 'sanctuary', None, None, [leonarda, donetella, michaelangela, rophel, splinker],
            [sai, nun_chuck, bostaff, sword])
sanctuary = Room("Sanctuary", 'sanctuary', "You leave the dark room to find yourself in a well lit tavern.\n"
                                           "There are people present who seem to be non-hostile."
                                           "They call the tavern Sanctuary.", 'echoing_room', None, None, None, None,
                 None, 'lego_room', None, [bar_tender, bar_patron], [health_potion, bigger_health_potion,
                                                                     stamina_potion, bigger_stamina_potion])
lego_room = Room("Child's Room", 'lego_room', "You enter a room that resembles one that would belong to a child.\n"
                                              " There are toys everywhere, especially the painful lego.",
                 'final_boss_room', None, None, 'room', None, None, None, None, None, [bonnet, rusty_dagger])
final_boss_room = Room("Final Boss Room", 'final_boss_room',
                       "You enter a room that the final boss resides in front of you, Captain Poof Wonder...\n"
                       "But he seems different.\n"
                       "He screams 'You were expecting a final boss, but it was I Dio.'", 'portal_room', None,
                       'lego_room',
                       None, None, 'hallway', None, None, [dio], [chicken_hat])
portal_room = Room("Portal Entrance", 'portal_room', "You walk into a room with a glowing red portal.", 'lava_room',
                   'final_boss_room', None, None, None, None, None, None, )
lava_room = Room("hOt RoOm", 'lava_room', "YoU entEr a roOm whEre iT Is sO hot thAt th3 c0nsoLe is LAGG1Ng.\n"
                                          "There is A man Wear!ng a W!nt3r c0at say1ng 'Man's not hot'",
                 None, None, None, None, None, None, None, None, [hot_mans], [boots4, helmet4, breastplate4, leggings4])
hall_way = Room("Dark Hallway", 'hallway', "You enter a dark hallway.\n"
                                           "Suddenly you here a man charging at you screaming 'I'm Useful!'", None,
                None, None, None, None, None, 'shrine', 'final_boss_room', [mj])
shrine = Room("Shrine", 'shrine', "You enter the room with an eerie presence.\n"
                                  "The presence seems to come from the shrine in front of you.\n"
                                  "There is a picture of Dio.", None, 'dark_corridor', None, None, 'hallway', None,
              None, None, [worshipper1, worshipper2, worshipper3, worshipper4, worshipper5])
dark_corridor = Room("Dark Corridor", 'dark_corridor',
                     "You walk into a dark room with a man slowly moon walking towards you.\n"
                     "He gradually comes closer with each 'Hee Hee' becoming louder.", 'shrine', None, None, None,
                     None, None, None, 'dark_room')
dark_room = Room("Dark Room", 'dark_room', "You enter a dark room with only one entrance.\n"
                                           "Suddenly a Dwarf hops out of the darkness and steals an item.",
                 None, None, None, None, None, 'dark_corridor', None, None, [dwarf])
current_node = room


def combat(target):
    print("A wild %s appears!" % target.name)
    first_strike = random.choice(["you", "enemy"])
    first_turn = True
    flee = False
    while main_character.health > 0 and target.health > 0 and not flee:
        if first_strike == 'you' or not first_turn:
            print("What do you do?")
            combat_command = input(">_").lower()
            if combat_command == 'attack':
                main_character.attack(target)
            if combat_command == 'flee':
                print("You attempt to flee")
                flee = main_character.flee()
                if flee:
                    continue
            else:
                print("You hesitate")

        if target.health > 0:
            target.attack(main_character)
        if main_character.health <= 0:
            print("You died.")
            quit(0)
        first_turn = False


inventory = []

while True:
    # Prints room information
    print(current_node.name)
    print(current_node.description)
    # print("You can go %s" % ", ".join(list(directions in current_node)))
    # leg_status = 'crawl'

    # Check for hostile characters
    if current_node.characters is not None:
        for character in current_node.characters:
            if character.mode == 'hostile':

                combat(character)

    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_direction:
        # Look for which command we typed in
        pos = short_direction.index(command)
        # Change the command to be the long form
        command = directions[pos]

    # Handles Movement
    if command in directions:
        try:
            current_node.move(command)
            if current_node == sewer_maintenance:
                print(sewer_maintenance.name)
                print("You fall down the manhole and break your legs.")
                print("You can no longer walk.")
            if current_node == lair:
                print("You %s into the room")
        except KeyError:
            print("You cannot go that way.")

    # Handles taking items
    elif "take" in command:
        if command[5:] == '':
            print("Take what?")
        item_requested = command[5:]
        for item_ in current_node.item:
            if item_.name.lower() == item_requested.lower():
                main_character.take(item_)

    elif "drop" in command:
        item_requested = command[5:]
        for item_ in inventory:
            if item_.name.lower() == item_requested.lower():
                main_character.drop(item_)
    elif "inventory" in command:
        main_character.view_inventory(inventory)
    else:
        print('Command Not Recognized.')
    print()
