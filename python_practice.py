import random
import os
import shutil
## nested loops

# rows = int(input("How many rows: "))
# columns = int(input("Columns: "))
# sym = input("Symbol: ")
#
#
# def matrix():
#     for i in range(rows):
#         for j in range(columns):
#             print(sym, end="")
#         print()
#
#
# matrix()
#
# ## loop control statements
# """
# break is used to terminate the loop
# continue skips to the next iteration of the loop
# pass does nothing
# """
#
# while True:
#     name = input(" Enter your name:")
#     if name != "":
#         break
#
# phone_number = "123-456-8933"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")
#
# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)
#
# ## 2D lists/ =multi dimensional lists
#
# drinks = ["coffee", "soda", "tea", "water"]
# dinner = ["pizza", "cheese", "orange"]
# dessert = ["orange", "cakes", "pie", "ice cream"]
#
# food = [drinks, dinner, dessert]
#
# print(food[0][0])
#
# ## dictionary
#
# capitals = {'USA': 'Washington DC',
#             'India':'New Dehli',
#             'China':'Beijing',
#             'Russia':'Moscow'}
#
# # print(capitals['Russia'])
# ## safer method, returns none if there is no key
# capitals.update({'Germany': 'Berlin',})
# print(capitals.get('Germany'))
# capitals.update({'USA': 'Seattle'})
# capitals.pop('China')
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# capitals.clear()
#
# for key, value in capitals.items():
#     print(key, value)
#
# ## index operators
#
# name = "Fred Fredburger"
#
# if name[0].islower():
#     name = name.capitalize()
#
# first_name = name[:5].upper()
# last_name = name[7:].lower()
# last_characters = name[-1]
#
# print(first_name)
# print(last_name)
#
# ## String formatting method
#
# # animal = "cow"
# # item = "moon"
#
# # print("The "+animal+" jumped over the "+item)
# # print("The {1} jumped over the {0}".format(animal, item))
# # print("The {1} jumped over the {0}".format(animal, item))
# print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))
#
# # text ="The {} jumped over the {}"
# # print(text.format(animal, item))
#
# name = "Dan"
# ## adding space to the name
# ## addin:< space to the name
# print("Hello ny mae is {:10}".format(name))
# print("Hello ny mae is {:<10}".format(name))
# print("Hello ny mae is {:>10}".format(name))
# print("Hello ny mae is {:^10}".format(name))
#
# number = 3.14159
# ## this shows two decimal numbers and rounds them
# print("The number pi is {:.2f}".format(number))
# ## prints binary representation of the number
# number2 = 3200
# print("The number2 is {:b}".format(number2))
# ## octal representation of the number
# print("The number2 is {:o}".format(number2))
# ##hexadecimal
# print("The number2 is {:x}".format(number2))
#
# ## random numbers
# x = random.randint(1, 10)
# y = random.random()
#
# myList  = ['rock', 'papers', 'scissors']
# z = random.choice(myList)
# cards = [1,2,3,4,5,6,7,8,9,10]
# random.shuffle(cards)
# print(cards)
# print(x)
#
# ## exception handling
# try:
#     numerator = int(input("Enter"))
#     denominator = int(input("Enter"))
#     result = numerator / denominator
#     print(result)
#     ## if user divides hy 0
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print(result)
# finally:
#     print("this will always execute")
path = "text.txt"
path2 = "testdir"

if os.path.exists(path):
    print(True)
    if os.path.isfile(path):
        print(True)
    if os.path.isdir(path2):
        print(True)
else:
    print("That location doesn't exist")
try:
    with open(path, "r") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)

print(file.closed)
## append
with open(path, "a") as file:
    file.write(f'{random.randint(0, 100)}')

"""
Copying with Shutil

copyfile() = copies contents of a file
copy() copyfile() with permission mode and destination can be a directory
copy2()  -= copy() and copies metadata of the file
"""

shutil.copyfile('text.txt', 'testdir/copy.txt')

"""Moving Files"""

source = "testdir/copy.txt"
destination = "movedcopy.txt"

try:
    if os.path.exists(destination):
        print("there is already a file here")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError as e:
    print(e)

try:
    if os.path.exists(destination):
        os.remove('movedcopy.txt')
        """remove directory"""
    # if os.path.exists("testdir"):
    #     os.rmdir("testdir")
    #     removes directory with files, be careful with this as it can delete everything in that folder
    #     shutil.rmtree("testdir")

except FileNotFoundError as e:
    print(e)

## modules is a file containing python code


