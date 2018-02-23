class Room(object):
    def __init__(self, name, room, description, north, south, east, west, north_west, north_east, south_east,
                 south_west):
        self.name = name
        self.room = room
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


# Initialize Rooms
room = Room("Room", 'room', "You are in a room with a torn up couch and claw marks on a wall.", None, 'echoing_room',
            'lego_room', None, None, 'steel_mill', None, None)
steel_mill = Room("Steel Mill", 'steel_mill', "You enter a room with the Orc Warlord Ukifak Lasgoni.", None, None, None,
                  'empty_room', None, None, 'room', None)
empty_room = Room("Empty Room", 'empty_room', "You enter an empty room all that is there is a button.", None, None,
                  'steel_mill', None, None, None, None, None)
echoing_room = Room("Echoing Room", 'echoing_room', "You enter an empty room. You feel an annoying presence.", 'room',
                    'sanctuary', None, 'well_lit_room', None, None, None, None)

