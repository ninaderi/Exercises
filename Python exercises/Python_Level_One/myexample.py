print(len("Hello World!"))
print(2+1)
# SLICING
mystring = "Salute"
print(mystring[-1])

mystring = "abcdefghij"
print(mystring[4:7:2])
print(mystring[::-1])
print(mystring+mystring)
print(mystring.upper())
print(mystring.split("e"))

username = "Sammy"
color = "green"
print(f"The {username} chose {color}")

mylist = [100, 20.1, "hello"]
print(mylist[2])
mylist.append("y")
print(mylist)
mylist.insert(1, "y")
print(mylist)
popped_item = mylist.pop(1)
print(mylist)
print(popped_item)

mylist1 = [0,1,2]
mylist2 = [3,4,5]
mylist3 = [6,7,8]

mega_list = [mylist1,mylist2,mylist3]
print(mega_list[2][1])

d = {"key1" : "value1", "key2" : "value2"}
print(d["key1"])

salaries = {"John" :20, "Sally": 30, "Sammy":15}
salaries["Cindy"] = 100 #This is to add to the dictionary
print(salaries["Cindy"])
salaries["John"] = salaries["John"] + 40 #This is to increase the value
print(salaries["John"])

people = {"John" :{"salary":10, "age" :30}}
print(people["John"]["salary"])

d = {"k1":10, "k2":20, "k3":30}
print(d.keys())
print(d.items())

#Tuples
t = (1,2,3)
mylist = [1,2,3]
mylist[0] = "New"
print(mylist) #But if you print(t) you will get an error

#Sets
mylist = [1,2,3,4,5,5,5,5,26,16,16,7,7,9]
print(set(mylist))

#Loops
seq = [1,2,3,4,5]
for jellyFish in seq:
    print(jellyFish)
for num in seq:
    print("Hello")

salaries = {"John":10, "Sally":20, "Lisa":30}
for employee in salaries:
    print(employee)
    print(salaries[employee])
#Tuple unpacking
mypairs = [("a",1),("b",2),("c",3)]
for item1,item2 in mypairs:
    print(item1)
    print(item2)

for x in range(0,11,2):
    print(x)

mylist = ["a","b","c"]
for index,item in enumerate(mylist):
    print(item)
    print(f"is at index {index}")
    print("")

def code_maker(mystring):
    output = list(mystring)
    for index,letter in enumerate(mystring):
     for vowel in "aeiou":
         if letter.lower()==vowel:
             output[index] = "x"
    output = "".join(output)
    return output
print(code_maker("Adam"))
