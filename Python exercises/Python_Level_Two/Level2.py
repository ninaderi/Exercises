#Scope
#LEGB - Locally, Enclosing, Globally, Built in

#OOP
class Dog():
    #Class Object Attributes
    species = "mammal"
    def __init__(self,input_breed,input_name):
        self.breed = input_breed
        self.name = input_name
x = Dog(input_breed="Cuttie",input_name="Sammy")
print(x.breed)
print(x.name)
print(x.species)

class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * self.pi
mycircle = Circle(10)
print(mycircle.radius)
print(mycircle.area())

class Animal():
    def __init__(self,fur):
        self.fur = fur
        print("Animal Created!")
    def report(self):
        print("Animal")
    def eat(self):
        print("Eating!")

class Dog(Animal):
    def __init__(self,fur):
        Animal.__init__(self,fur)
        print("Dog is created!")
    def report(self):
        print("I am a dog!")
a = Animal("Fuzzy")
a.report() #Notic that I don't have to type "print" because I already have print inside those methods
a.eat()

d = Dog("Furry")
d.eat()
d.report()
print(d.fur)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    # def __repr__(self):
    #     # return f"Titel: {self.title}, Author: {self.author}"
    def __len__(self):
        return self.pages
mybook = Book("Python finally!","Jose",250)
print(mybook)
length_book = len(mybook)
print(length_book)

# Decorators
def hello(name="Jose"):
    print("the hello()func has been run")
    def greet():
        return "    This is inside the greet()"
    def welcome():
        return "    This is inside welcome()"
    if name=="Jose":
        return greet
    else:
        return welcome
x = hello(name="Sammy")
print(x())

def hello():
    return "Hi Jose"
def other(func):
    print("Some other code")
    #Assume that fun passed in is a function
    print(func())
other(hello)

def new_decorator(func):
    def wrap_func():
        print("Some code before executing func()")
        func()
        print("Code here, after executing func()")
    return wrap_func
# @new_decorator
def func_needs_decorator():
    print("Please decorate me!!!")
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
