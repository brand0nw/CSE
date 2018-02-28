class Room(object):
    def __init__(self, name, location, description, north, south, east, west, north_west, north_east, south_east,
                 south_west):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


directions = ('north', 'south', 'east', 'west', 'north_west', 'north_east', 'south_east', 'south_west')

# Initialize Rooms
room = Room("Room", 'room', "You are in a room with a torn up couch and claw marks on a wall.", None, 'echoing_room',
            'lego_room', None, None, 'steel_mill', None, None)
steel_mill = Room("Steel Mill", 'steel_mill', "You enter a room with the Orc Warlord Ukifak Lasgoni.", None, None, None,
                  'empty_room', None, None, 'room', None)
empty_room = Room("Empty Room", 'empty_room', "You enter an empty room all that is there is a button.", None, None,
                  'steel_mill', None, None, None, None, None)
echoing_room = Room("Echoing Room", 'echoing_room', "You enter an empty room. You feel an annoying presence.", 'room',
                    'sanctuary', None, 'well_lit_room', None, None, None, None)
well_lit_room = Room("Well Lit Room", 'well_lit_room', "You enter a well lit room with a heavily armored JoJo."
                                                       "He seems aggressive as he mutters 'Omae wa moe shinderu'.",
                     None, None, 'echoing_room', 'vault',
                     None, None, None, None)
vault = Room("Vault of Undeniably Valuable Really Long Name Loot", 'vault',
             "You enter a room filled with gold."
             "In the center of the room there is a pedestal."
             "In the pedestal there is a weapon.", None, 'sewer_maintenance', 'well_lit_room', None, None, None, None,
             None)
sewer_maintenance = Room("Sewer Maintenance", 'sewer_maintenance',
                         "You fall down a hole and break your legs there is no way out."
                         "The room is dark, you feel a hostile presence.", None, None, 'lair',
                         None, None, None, None, None)
lair = Room("Lair", 'lair', "The room is dark, there are four shadowy figures who begin to approach you.", None, None,
            None, None, None, 'sanctuary', None, None)
sanctuary = Room("Sanctuary", 'sanctuary', "You leave the dark room to find yourself in a well lit tavern."
                                           "There are people present who seem to be non-hostile."
                                           "They call the tavern Sanctuary.", None, None, None, None, None, None,
                 'lego_room', None)
lego_room = Room("Child's Room", 'lego_room', "You enter a room that resembles one that would belong to a child."
                                              " There are toys everywhere, especially the painful lego.",
                 'final_boss_room', None, None, 'room', None, None, None, None)
final_boss_room = Room("Final Boss Room", 'final_boss_room',
                       "You enter a room that the final boss resides in front of you, Captain Poof Wonder..."
                       "But he seems different."
                       "He screams 'You were expecting a final boss, but it was I Dio.'", 'portal_room', None, None,
                       None, None, 'hallway', None, None)
portal_room = Room("Portal Entrance", 'portal_room', "You walk into a room with a glowing red portal.", 'lava_room',
                   None, None, None, None, None, None, None, )
lava_room = Room("hOt RoOm", 'lava_room', "YoU entEr a roOm whEre iT Is sO hot thAt th3 c0nsoLe is LAGG1Ng."
                                          "There is A man Wear!ng a W!nt3r c0at say1ng 'Man's not hot'",
                 None, None, None, None, None, None, None, None)
hall_way = Room("Dark Hallway", 'hallway', "You enter a dark hallway."
                                           "Suddenly you here a man charging at you screaming 'I'm Useful!'", None,
                None, None, None, None, None, 'shrine', 'final_boss_room')
shrine = Room("Shrine", 'shrine', "You enter the room with an eerie presence."
                                  "The presence seems to come from the shrine in front of you."
                                  "There is a picture of Dio.", None, 'dark_corridor', None, None, 'hallway', None,
              None, None)
dark_corridor = Room("Dark Corridor", 'dark_corridor',
                     "You walk into a dark room with a man slowly moon walking towards you."
                     "He gradually comes closer with each 'Hee Hee' becoming louder.", 'shrine', None, None, None,
                     None, None, None, 'dark_room')
dark_room = Room("Dark Room", 'dark_room', "You enter a dark room with only one entrance."
                                           "Suddenly a Dwarf hops out of the darkness and steals an item.",
                 None, None, None, None, None, 'dark_corridor', None, None)
current_node = room

while True:

    print(current_node.name)
    print(current_node.description)

    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            current_node.move(command)
            if current_node == sewer_maintenance:
                print("You fall down the manhole and break your legs.")
                print("You can no longer walk.")
                leg_status = 'crawl'
                print("You %s into the room" % leg_status)
        except KeyError:
            print("You cannot go that way.")
    else:
        print('Command Not Recognized.')
    print()
