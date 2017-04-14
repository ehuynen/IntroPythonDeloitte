class Animal (object):
    def __init__(self, startname, age):
        self.name = startname
        self.age = age
    def description(self):
        print("This is "+ self.name)
        print("He/she is " + str(self.age)+" years old.")

