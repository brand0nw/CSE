# import winsound

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
            'SOUTH': 'SEWERMAINTENANCE',
        }
    },
    'SEWERMAINTENENCE': {
        'NAME': "Sewer Maintenance",
        'DESCRIPTION': "You fall down a hole and break your legs there is no way out.\n"
                       "The room is dark, you feel a hostile presence.",
        'PATHS': {
            'EAST': 'LAIR'
        }
    },
    'LAIR': {
        'NAME': "Lair",
        'DESCRIPTION': "The room is dark and there are four shadowy figures who begin to approach you.",
        'PATHS': {
            'NORTHEAST': 'SANCTUARY',
        }
    },
    'SANCTUARY': {
            'NAME': "Sanctuary for People",
            'DESCRIPTION': "You leave the dark room to find yourself in a well lit tavern.\n"
                           "There are people present who seem to be non-hostile.\n"
                           "They call the tavern Sanctuary.",
            'PATHS': {
                'SOUTHEAST': 'LEGOROOM'
            }
    },
    'LEGOROOM': {
            'NAME': "Child's Room",
            'DESCRIPTION': "You enter a room that resembles one that would belong to a child.\n"
                           "There are toys everywhere, especially the painful lego.",
            'PATHS': {
                'WEST': 'ROOM',
                'NORTH': 'FINALBOSSROOM'
            }
    },
    'FINALBOSSROOM': {
                'NAME': "Final Boss Room",
                'DESCRIPTION': "You enter a room that the final boss resides in front of you, Captain Poof Wonder...\n"
                               "But he seems different.\n"
                               "He screams 'You were expecting a final boss, but it was I Dio.'",
                'PATHS': {
                    'NORTHEAST': 'HALLWAY',
                    'NORTH': 'PORTALROOM'
                }
    },
    'PORTALROOM': {
        'NAME': "Portal Entrance",
        'DESCRIPTION': "You walk into a room with a glowing red portal.",
        'PATHS': {
            'NORTH': 'LAVAROOM'
        }
    },
    'LAVAROOM': {
        'NAME': "hOt RoOm",
        'DESCRIPTION': "YoU entEr a roOm whEre iT Is sO hot thAt th3 c0nsoLe is LAGG1Ng.\n"
                       "There is A man Wear!ng a W!nt3r c0at say1ng 'Man's not hot'",
        'PATHS': {
        }
    },
    'HALLWAY': {
        'NAME': "Dark Hallway",
        'DESCRIPTION': "You enter a dark hallway.\n"
                       "Suddenly you here a man charging at you screaming 'I'm Useful!'",
        'PATHS': {
            'SOUTHEAST': 'SHRINE',
            'SOUTHWEST': 'FINALBOSSROOM'
        }
    },
    'SHRINE': {
        'NAME': "Shrine",
        'DESCRIPTION': "You enter the room with an eerie presence.\n"
                       "The presence seems to come from the shrine in front of you.\n"
                       "There is a picture of Dio.",
        'PATHS': {
            'SOUTH': 'DARKCORRIDOR',
            'NORTHWEST': 'HALLWAY'
        }
    },
    'DARKCORRIDOR': {
        'NAME': "Dark Corridor",
        'DESCRIPTION': "You walk into a dark room with a man slowly moon walking towards you.\n"
                       "He gradually comes closer with each 'Hee Hee' becoming louder.",
        'PATHS': {
            'SOUTHWEST': 'DARKROOM'
        }
    },
    'DARKROOM': {
        'NAME': "Dark Room",
        'DESCRIPTION': "You enter a dark room with only one entrance.\n"
                       "Suddenly a Dwarf hops out of the darkness and steals an item.",
        'PATHS': {
        }
    },
}
current_node = world_map['ROOM']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHWEST', 'NORTHEAST', 'SOUTHWEST', 'SOUTHEAST']
leg_status = 'walk'
OP_weapon = 'Melon Bratch'

# winsound.PlaySound('hehe.mp3', winsound.SND_FILENAME)

while True:

    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])

    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            if current_node == 'VAULT' and name_of_node == 'MANHOLE':
                print("You fall down the manhole and break your legs.")
                print("You can no longer walk.")
                leg_status = 'crawl'
                print("You %s into the room" % leg_status)
            current_node = world_map[name_of_node]

        except KeyError:
            print("You cannot go that way.")
    else:
        print('Command Not Recognized.')
    print()
