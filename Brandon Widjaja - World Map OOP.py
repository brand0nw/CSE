import random


class Character(object):
    def __init__(self, name, race, occupation, mode, status, attack, health=100, money=0):
        self.name = name
        self.race = race
        self.occupation = occupation
        self.mode = mode
        self.status = status
        self.attack = attack
        self.health = health
        self.money = money

    def attack(self, target):
        if target.status == 'dead':
            print(target.name + " is already dead")
            return
        if self.mode in ['hostile', 'neutral']:
            target.take_damage(self.attack)
            print("You attack.")
            print("It hits.")
        else:
            print("You miss.")

    def dodge(self, dodge_chance):
        if self.attack in ['hostile', 'neutral']:
            dodge_chance = random.randint(1, 5)

    def defend(self, me):
        if self.mode in ['hostile', 'neutral']:
            me.dodge(self.defend)
            print("You defend.")
            print("You successfully defended yourself.")
        else:
            print("It connects you have been hit")

    def take_damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            print(self.name + " has died")
            self.status = 'dead'


main_chracter = Character("Dave", 'nugu', 'radish_farmer', 'you', 'alive', 'something')
bar_tender = Character("Matilda", 'human', 'bar_tender', 'friendly', 'alive', None, money=9999999)
bar_patron = Character("Craig", 'elf', 'bum', 'friendly', 'alive', None)
boss1 = Character("Ukifak Lasgoni", 'orc', 'war_lord', 'hostile', 'alive', 'swing', 200000)
boss2 = Character("JoJo", 'human', '?', 'hostile', 'alive', 'punch', 1000000)
final_boss = Character("Captain Poof Wonder", 'human', 'knight_captain', 'hostile', 'deceased', None)
dio = Character("Dio", 'human', 'annoyance', 'hostile', 'alive', 'swing', 1000)
leonarda = Character("Leonarda", 'tortoise', 'ninja', 'neutral', 'alive', 'swipe')
donetella = Character("Donatella", 'tortoise', 'ninja', 'neutral', 'alive', 'swing')
michaelangela = Character("Michaelangela", 'tortoise', 'ninja', 'neutral', 'alive', 'swing')
rophel = Character("Rophel", 'tortoise', 'ninja', 'neutral', 'alive', 'stab')
splintar = Character("Splintar", 'rat', 'unknown', 'friendly', 'alive', None)
hot_mans = Character("Lil' RiceGrain", 'human', 'rapper', 'neutral', 'alive', 'shoot', 2)
dwarf = Character("Harold", 'dwarf', 'theif', 'hostile', 'alive', 'shank')
worshipper1 = Character("Kristofer", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10)
worshipper2 = Character("Lonny", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10)
worshipper3 = Character("Eliseo", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10)
worshipper4 = Character("Ibrahim", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10)
worshipper5 = Character("Dante", 'human', 'worshipper', 'neutral', 'alive', 'punch', 10)
osian = Character("Katou", 'orange_beast', 'jerk', 'hostile', 'alive', 'swipe', 999999999999999999999999999999999999999)
mj = Character("Michael Jackson", 'human', 'singer', 'hostile', 'alive', 'flick', 10000000)





class Room(object):
    def __init__(self, name, location, description, north, south, east, west, north_west, north_east, south_east,
                 south_west, characters=None):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


directions = ['north', 'south', 'east', 'west', 'north_west', 'north_east', 'south_east', 'south_west']
short_direction = ['n', 's', 'e', 'w', 'nw', 'ne', 'se', 'sw']

# Initialize Rooms
room = Room("Room", 'room', "You are in a room with a torn up couch and claw marks on a wall.", None, 'echoing_room',
            'lego_room', None, None, 'steel_mill', None, None, )
steel_mill = Room("Steel Mill", 'steel_mill', "You enter a room with the Orc Warlord Ukifak Lasgoni.", None, None, None,
                  'empty_room', None, None, 'room', None, [boss1])
empty_room = Room("Empty Room", 'empty_room', "You enter an empty room all that is there is a button.", None, None,
                  'steel_mill', None, None, None, None, None)
echoing_room = Room("Echoing Room", 'echoing_room', "You enter an empty room. You feel an annoying presence.", 'room',
                    'sanctuary', None, 'well_lit_room', None, None, None, None, [osian])
well_lit_room = Room("Well Lit Room", 'well_lit_room', "You enter a well lit room with a heavily armored JoJo.\n"
                                                       "He seems aggressive as he mutters 'Omae wa moe shinderu'.",
                     None, None, 'echoing_room', 'vault',
                     None, None, None, None, [boss2])
vault = Room("Vault of Undeniably Valuable Really Long Name Loot", 'vault',
             "You enter a room filled with gold.\n"
             "In the center of the room there is a pedestal.\n"
             "In the pedestal there is a weapon.", None, 'sewer_maintenance', 'well_lit_room', None, None, None, None,
             None)
sewer_maintenance = Room("Sewer Maintenance", 'sewer_maintenance',
                         "You fall down a hole and break your legs there is no way out.\n"
                         "The room is dark, you feel a hostile presence.", None, None, 'lair',
                         None, None, None, None, None)
lair = Room("Lair", 'lair', "The room is dark, there are four shadowy figures who begin to approach you.", None, None,
            None, None, None, 'sanctuary', None, None, [leonarda, donetella, michaelangela, rophel, splintar])
sanctuary = Room("Sanctuary", 'sanctuary', "You leave the dark room to find yourself in a well lit tavern.\n"
                                           "There are people present who seem to be non-hostile."
                                           "They call the tavern Sanctuary.", 'echoing_room', None, None, None, None,
                 None, 'lego_room', None, [bar_tender, bar_patron])
lego_room = Room("Child's Room", 'lego_room', "You enter a room that resembles one that would belong to a child.\n"
                                              " There are toys everywhere, especially the painful lego.",
                 'final_boss_room', None, None, 'room', None, None, None, None)
final_boss_room = Room("Final Boss Room", 'final_boss_room',
                       "You enter a room that the final boss resides in front of you, Captain Poof Wonder...\n"
                       "But he seems different.\n"
                       "He screams 'You were expecting a final boss, but it was I Dio.'", 'portal_room', None,
                       'lego_room',
                       None, None, 'hallway', None, None, [final_boss, dio])
portal_room = Room("Portal Entrance", 'portal_room', "You walk into a room with a glowing red portal.", 'lava_room',
                   'final_boss_room', None, None, None, None, None, None, )
lava_room = Room("hOt RoOm", 'lava_room', "YoU entEr a roOm whEre iT Is sO hot thAt th3 c0nsoLe is LAGG1Ng.\n"
                                          "There is A man Wear!ng a W!nt3r c0at say1ng 'Man's not hot'",
                 None, None, None, None, None, None, None, None, [hot_mans])
hall_way = Room("Dark Hallway", 'hallway', "You enter a dark hallway.\n"
                                           "Suddenly you here a man charging at you screaming 'I'm Useful!'", None,
                None, None, None, None, None, 'shrine', 'final_boss_room')
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

while True:

    print(current_node.name)
    print(current_node.description)

    leg_status = 'crawl'

    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_direction:
        # Look for which command we typed in
        pos = short_direction.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
            if current_node == sewer_maintenance:
                print(sewer_maintenance.name)
                print("You fall down the manhole and break your legs.")
                print("You can no longer walk.")
            if current_node == lair:
                print("You %s into the room" % leg_status)
        except KeyError:
            print("You cannot go that way.")
    else:
        print('Command Not Recognized.')
    print()
