# import random
import string
# # print("Hello World")
# #
# # # Brandon
# #
# # print(3 + 5)
# # print(7 ^ 6)
# # print(9/8)
# # print(3 ** 2)
# #
# # # this makes a new line. In python 3.6, it looks like: print()
# # print("See if you can figure this out")
# # print(13 % 12)
# # print(15 % 5)
# # print(14 % 5)
# # print(13 % 5)
# # print(12 % 5)
# # print(11 % 5)
# # print(10 % 5)
# # print(9 % 5)
# #
# # car_name = "Retractor"
# # car_type = "Ford Gran Torino"
# # car_cylinders = 8
# # car_mpg = 9000.1
# #
# # # Inline printing
# # print("I have a car called the %s. It's a %s." % (car_name, car_type))
# #
# # # Asking for input
# #
"""
name = input("What is your name? ")  # In python 3, it is just called input()
print("Hello %s." % name)

age = input("How old are you? ")
print("%s?! DAYUM you old." % age)
# #
#
# # Functions
#
#
# # def print_hw():
# #     print("Hello World")
# #
# #
# # print_hw()
# # print_hw()
# # print_hw()
# #
# #
# # def say_hi(name):  # name is a parameter
# #     print("Hello %s" % name)
# #     print("Enjoy your day.")
# #
# #
# # say_hi("John")
# #
# #
# # def print_age(name, age):
# #     print("%s is %d years old." % (name, age))
# #     age += 1  # age = age + 1
# #     print("Next year, they will be %d" % age)
# #
# #
# # print_age("John", 15)
# #
# #
# # def f(x):
# #     return x**3 + 4 * x**2 + 7 * x - 4
# #
# #
# # print(f(3))
# # print(f(4))
# # print(f(5))
# #
# #
# # # If statements
# #
# #
# # def grade_calc(percentage):
# #     if percentage >= 90:
# #         return "A"
# #     elif percentage >= 80:
# #         return "B"
# #     elif percentage >= 70:
# #         return "C"
# #     elif percentage >= 60:
# #         return "D"
# #     else :
# #         return "F"
#
#
# # Function
#
#
# def happy_bday(name):
#     print("Happy Birthday to you" + ",")
#     print("Happy Birthday to you" + ",")
#     print("Happy Birthday to " + name + ",")
#     print("Happy Birthday to you" + ".")
#
#
# happy_bday("Mr.Grinch")
#
#
# # Loops
#
# for num in range(10):
#     print(num + 1)
#
# # DO NOT RUN!!!
#
#
# # a = 1
# # while a <= 10:
# #     print(a)
# #     a += 1
#
#
# # Random Number
#
#  # This should be on line 1
# print(random.randint(0,100))

# Comparisons
print(1 == 1) # Is 1 equal to 1?
print(1 != 2) # Is 2 not equal to 2?
print(10 <= 15)
print(not False)

# Recasting
c = '1'
print(c == 1)
print(int(c) == 1)
print(c == str(1))

# The input command ALWAYS gives a string

# Generate 2 numbers between 1 and 6 then print it on the line below it. Add then together

"""

# Lists
the_count = [1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Egg rolls", "Milk", "Rice", "Soda", "Chips"]

print(shopping_list[2])

print(len(shopping_list))

# Going through a list
# for item in shopping_list:
#     print(item)

for num in the_count:
    print(num * 2)

len(shopping_list)  # Gives me the length of the list
range(3)  # Gives a list of numbers 0 to 2
range(len(shopping_list))  # A list of EVERY index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item at index %d is %s" % (num, item))

# Turn things into a list
str1 = "Hello Class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))

# Add things to a list
shopping_list.append("cereal")
print(shopping_list)

shopping_list.append("Uranium")
print(shopping_list)

# Removing things from a list
shopping_list.remove("Soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

# the string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

# Dealing with strings
strTwo = "Tachanka iS tHe LoRd anD SaViOr"
lowercase = strTwo.lower()
print(lowercase)

# Dictionaries - Made up of Key: Value pairs
dictionary = {'name': 'Lance', 'age': 23, 'height': 5 * 12 + 7}

# Accessing dictionaries
print(dictionary['name'])
print(dictionary['age'])
print(dictionary['height'])

# Adding to a dictionary
dictionary['weight'] = 280
print(dictionary)
large_dictionary = {
    'CA': 'California',
    'FL': 'Florida',
    'OH': 'Ohio'
}
oof = [1, 2]
print(large_dictionary['FL'])

larger_dictionary = {
    'CA': [
        'Fresno',
        'Sacramento',
        'Los Angeles'
    ],
    'FL': [
        'Tampa',
        'Orlando',
        'Miami'
    ],
    'OH': [
        'Cleavland',
        'Cincinnati',
    ]
}

print(larger_dictionary['FL'])
print(larger_dictionary["FL"][2])

print(larger_dictionary["OH"][1])

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}

current_node = largest_dictionary['CA']
print(current_node)
print(current_node['NAME'])
print(current_node['POPULATION'])
