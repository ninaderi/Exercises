# for item in [1,2,3]:
#     print(i)


x = 0
while x < 3:
    print("Smallerrrrr")
    x = x + 1

# Looping multiple sequences
a = ['a', 'b', 'c']
b = [1, 2, 3]
for i, j in zip(a, b):
    print("%s is %s" % (i, j))
