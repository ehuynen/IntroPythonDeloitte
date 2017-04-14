class Animal (object):
    def __init__(self, startname, age):
        self.name = startname
        self.age = age
    def description(self):
        print("this is "+ self.name)
        print("He/she is " + str(self.age)+" years old.")

lion = Animal("Harry", 11)
print(lion.description)