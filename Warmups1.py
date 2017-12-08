# def reverse_order(first_name, last_name):
#     # print("%s, %s" % (last_name, first_name))
#     print(last_name + " " + first_name) # Concatenation

# def reverse_order():
#     first_name =input("First name")
#     last_name = input("Last_name")
#     print("%s, %s" % (last_name, first_name))


# 12.5.17


# def add_py(name):
#     print("%s.py" % name)
#     print(name + ".py")


# 12.6.17


def add(num1, num2, num3):
    print(num1 + num2 + num3)


add(5, 6, 69)


# 12.7.17

def repeat(string):
    print(string)
    print(string)
    print(string)

    for x in range(3):
        print(string)


repeat("Hello")

# 12.8.17


def date(month, day, year):
    print(str(month) + "/" + str(day) + "/" + str(year))


date(12, 8, 17)