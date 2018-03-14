class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def write(self):
        print("%s goes to write" % self.name)


class Programmer(Employee):
    def __init__(self, name, age, height, good_pay):
        super(Programmer, self).__init__(name, age, height)
        self.good_pay = good_pay

    def type(self):
        print("%s goes to type" % self.type)
