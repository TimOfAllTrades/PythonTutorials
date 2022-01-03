#An object holds properties (variables) and functions
#Objects can also be represented as variables

#Variables properties within an object are called instance variables or attributes
#Functions within an object are called methods

#Classes are blueprints or templates where objects can be made.
#A constructor adds the initial variables.

class Robot0:    #This is a class with attributes and no constructor

    name = "Spike"    #These are attributes
    color = "yellow"    #These are attributes
    weight = 60    #These are attributes

    def introduce_self(self):    #This is a method
        print("My name is " + self.name) #Self refers to the object it that is being run

class Robot1:    #This is a class without attributes and no constructor

    def introduce_self(self):    #This is a method
        print("My name is " + self.name) #Self refers to the object it that is being run

class Robot2:    #This is a class without attributes and no constructor

    def __init__(self, name, color, weight):    #This is a constructor
        self.name = name    
        self.color = color  
        self.weight = weight   

    def introduce_self(self):    #This is a method
        print("My name is " + self.name) #Self refers to the object it that is being run

class Robot3:    #This is a class without attributes and no constructor
    

    def __init__(self, name, color, weight):    #This is a constructor
        self.name = name    
        self.color = color  
        self.weight = weight
        self.actualweight = weight + 10 #Adding additional parameters or variables.
    
    

    def introduce_self(self):    #This is a method
        print("My name is " + str(self.actualweight)) #Self refers to the object it that is being run


#Creating an objection without a class constructor with predefined attributes
r0 = Robot0()
r0.introduce_self()

#Creating an object without a class constructor
r1 = Robot1()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30
r1.introduce_self()

#Creating an object with a class constructor
r2 = Robot2("Jerry","blue",30)

r2.introduce_self()

r3 = Robot3("Jerry","blue",30)
r3.introduce_self()
