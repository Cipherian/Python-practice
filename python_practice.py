import random
import os
import shutil
from abc import ABC, abstractmethod
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
# path = "text.txt"
# path2 = "testdir"
#
# if os.path.exists(path):
#     print(True)
#     if os.path.isfile(path):
#         print(True)
#     if os.path.isdir(path2):
#         print(True)
# else:
#     print("That location doesn't exist")
# try:
#     with open(path, "r") as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#
# print(file.closed)
# ## append
# with open(path, "a") as file:
#     file.write(f'{random.randint(0, 100)}')
#
# """
# Copying with Shutil
#
# copyfile() = copies contents of a file
# copy() copyfile() with permission mode and destination can be a directory
# copy2()  -= copy() and copies metadata of the file
# """
#
# shutil.copyfile('text.txt', 'testdir/copy.txt')
#
# """Moving Files"""
#
# source = "testdir/copy.txt"
# destination = "movedcopy.txt"
#
# try:
#     if os.path.exists(destination):
#         print("there is already a file here")
#     else:
#         os.replace(source, destination)
#         print(source+" was moved")
# except FileNotFoundError as e:
#     print(e)
#
# try:
#     if os.path.exists(destination):
#         os.remove('movedcopy.txt')
#         """remove directory"""
#     # if os.path.exists("testdir"):
#     #     os.rmdir("testdir")
#     #     removes directory with files, be careful with this as it can delete everything in that folder
#     #     shutil.rmtree("testdir")
#
# except FileNotFoundError as e:
#     print(e)

## modules is a file containing python code

## method chaining

# class Car:
#
#     def turn_on(self):
#         print("turning on")
#         return self
#
#     def drive(self):
#         print("drive")
#         return self
#
#     def brake(self):
#         print("braking")
#         return self
#
#     def turn_off(self):
#         print("turning off")
#         return self
#
# car = Car()
#
# car.turn_on().drive()
#
# car.turn_on()\
#     .drive().\
#     brake().\
#     turn_off()

# abstract classes
# abstract prevents a user from creating an object of that class
# abstract method is a method that h as a declaration but no implementation

# class Vehicle(ABC):
#
#     @abstractmethod
#     def go(self):
#         pass
#
# class Car(Vehicle):
#     def go(self):
#         print('Drive the car')
#
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print('You ride the motorcycle')

# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
# car.go()
# motorcycle.go()

## Pass objects as arguments

# class Car:
#     color = None
#
# class Motorcycle:
#     color = None
#
# def change_color(car, color):
#     car.color = color
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
# bike_1 = Motorcycle()
# change_color(car_1, "red")
# change_color(car_2, "green")
# change_color(car_3, "yellow")
# change_color(bike_1, "yellow")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)
#
#
# # Duck typing is the concept where the class of an object is less important than the methods or attributes of the class
#
# class Duck:
#
#     @staticmethod
#     def walk():
#         print("Duck walk")
#
#     @staticmethod
#     def talk():
#         print("Duck talk")
#
# class Chicken:
#
#     def walk(self):
#         print("chicken walk")
#
#     def talk(self):
#         print("chicken talk")
#
# class Hooman():
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("Hooman catch")
#
# duck = Duck()
# chicken = Chicken()
# hooman = Hooman()
#
# hooman.catch(chicken)

#walrus operator: assigns values to variables as part of a larger expression
# :=

# happy = True
# print(happy)

# print(happy := True)
# foods=list()
# while True:
#     food = input("What food do you want to eat?: ")
#     if food == "quit":
#         break
#     foods.append(food)
#
# foods = list()
# while food := input("What food do you want to eat?: ") != "quit":
#     foods.append(food)

#lambda function = writen in 1 line using lambda keyword
# useful if needed for one use

# def double(x):
#     return x*2

# double = lambda x: x * 2
# multiply = lambda x, y: x * y
# add = lambda x, y, z: x + y + z
# print(add(5,6,7))
#
# age_check = lambda age: True if age >= 18 else False
# print(age_check(18))
#
# ## sort iterables in python
#
# students = ['squidward','students', 'Sponge', 'Mr. Krabs']
#
# students.sort(reverse=True)
# sorted_students = sorted(students)
#
# for student in stored_students:
#     print(student)

# students = [("Squidward", "F", 60),
#             ("Sponge Bob", "A", 33),
#             ("Mr. Krabs", "D", 78),
#             ("Patrick", "C", 36),
#             ("Sandy", "A", 31)]
#
# grade = lambda grades:grades[1]
# students.sort(key=grade, reverse=True)
#
# for student in students:
#     print(student)
#
# age = lambda ages:ages[2]
# students.sort(key=age)
#
# for student in students:
#     print(student)

#map function in python
# map function in python accepts a function as an argument and an iterable map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 30.00),
         ("socks", 50.00)]

to_euros = lambda data: (data[0], data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]/0.82)

store_euros = list(map(to_dollars, store))

for i in store_euros:
    print(f'{i}')
