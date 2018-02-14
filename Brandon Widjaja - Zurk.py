world_map = {
    'ROOM': {
        'NAME': "Room",
        'DESCRIPTION': "You are in a room with a torn up couch and claw marks on a wall.",
        'PATHS': {
            'NORTHEAST': 'STEELMILL',
            'SOUTH': 'ECHOINGROOM',
            'EAST': 'LEGOROOM',
        }
    },
    'STEELMILL': {
        'NAME': "Steel Mill",
        'DESCRIPTION': "You enter a room with the Orc Warlord Ukifak Lasgoni.",
        'PATHS': {
            'WEST': 'EMPTYROOM',
            'SOUTHEAST': 'ROOM',
        }
    },
    'EMPTYROOM': {
        'NAME': "Empty Room",
        'DESCRIPTION': "You enter an empty room all that is there is a button.",
        'PATHS': {
            'EAST': 'STEELMILL',
        }
    },
    'ECHOINGROOM': {
        'NAME': "Echoing Room",
        'DESCRIPTION': "You enter an empty room. You feel an annoying presence.",
        'PATHS': {
            'NORTH': 'ROOM',
            'WEST': 'WELLLITROOM',
            'SOUTH': 'SANCTUARY',
        }
    },
    'WELLLITROOM': {
        'NAME': "Well Lit Room",
        'DESCRIPTION': "You enter a well lit room with a heavily armored JoJo.\n"
                       "He seems aggressive as he mutters 'Omae wa moe shinderu'.",
        'PATHS': {
            'EAST': 'ECHOINGROOM',
            'WEST': 'VAULT'
        }
    },
    'VAULT': {
        'NAME': "Vault of Undeniably Valuable Really Long Name Loot",
        'DESCRIPTION': "You enter a room filled with gold.\n"
                       "In the center of the room there is a pedestal.\n"
                       "In the pedestal there is a weapon",
        'PATHS': {
            ''
        }
    },
}
current_node = world_map['ROOM']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHWEST', 'NORTHEAST', 'SOUTHWEST', 'SOUTHEAST']

while True:

    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])

    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go that way.")
    else:
        print('Command Not Recognized.')
    print()
