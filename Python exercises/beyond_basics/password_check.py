correct_password = "python357"
name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password! Enter again: ")

# print("Hi", name, "You are logged in")
# String formatting is the right way to do this especially if we have multiple variables
message = "Hi %s %s, you are logged in" % (name, surname)
print(message)
