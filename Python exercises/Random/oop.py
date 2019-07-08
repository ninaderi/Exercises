class Dog:
    species = 'mammel'

    def __init__(self, name, age):
        self.name = name
        self.age = age

def get_biggest_number(*args):
    return max(args)

x = Dog("Cindy", 3)
y = Dog("Mikey", 5)
z = Dog("Sally", 7)

print("The oldest dog is {} years old.".format(get_biggest_number(x.age, y.age, z.age)))
