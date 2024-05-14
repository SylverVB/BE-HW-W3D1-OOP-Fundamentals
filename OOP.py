# Lesson 2: Assignment | OOP Fundamentals

# 1. City Infrastructure Management System
# Objective:
# The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated 
# City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures 
# to manage different aspects of a city, such as buildings, traffic, and events.

# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement 
# a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

# Code Example: Provide a basic structure for the Vehicle class without methods.
# ```python
# class Vehicle:
# def init(self, reg_num, type, owner):
# self.registration_number = reg_num
# self.type = type
# self.owner = owner
# ```

# Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of 
# Vehicle objects and updating their owners.

print("\nTASK 1")

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, type, owner):
         self.type = type
         self.owner = owner
         return f"The new {type} owner is {owner}\n"

Vehicle1 = Vehicle(34568, "car", "Victor")
print(f"\nThe vehicle registration number is {Vehicle1.registration_number}")
print(f"It is a {Vehicle1.type}")
print(f"The previous {Vehicle1.type} owner is {Vehicle1.owner}")
print(Vehicle1.update_owner("car", "Cait"))
Vehicle2 = Vehicle("005678", "truck", "Stephen")
print(f"The vehicle registration number is {Vehicle2.registration_number}")
print(f"It is a {Vehicle2.type}")
print(f"The previous {Vehicle2.type} owner is {Vehicle2.owner}")
print(Vehicle2.update_owner("truck", "John"))
Vehicle3 = Vehicle(859120, "bus", "Anthony")
print(f"The vehicle registration number is {Vehicle3.registration_number}")
print(f"It is a {Vehicle3.type}")
print(f"The previous {Vehicle3.type} owner is {Vehicle3.owner}")
print(Vehicle3.update_owner("bus", "Kevin"))

print("TASK 2\n")

# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method 
# add_participant that increases the count and a method get_participant_count to retrieve the current count.

# Code Example: Basic Event class without participant tracking.
# ```python
# class Event:
# def init(self, name, date):
# self.name = name
# self.date = date
# ```

class Event:
    
    def __init__(self, name, date, number_of_seats):
        self.name = name
        self.date = date
        self.number_of_seats = number_of_seats
        self.number_of_participants = 10     # Assume that there were initially 10 participants at the event who joined on May 13. 
                                             # Do not count Victor here because he is a host at the event
    
    def add_participant(self, name, date):
        print(f"{name} joined the event on {date}")
        self.number_of_participants += 1
        self.number_of_seats -= 1
    
    def get_participant_count(self):
        print(f"\nThe current number of participants is {self.number_of_participants}")
        print(f"The number of remaining seats is {self.number_of_seats - 10}\n")

scientific_week = Event("Victor", "May 13", 25)
print("Existing participants:\n")
print(f"{scientific_week.name} joined the event as a host on {scientific_week.date}\n")
print("New participants:\n")
scientific_week.add_participant("Alice", "May 14")
scientific_week.add_participant("Cait", "May 14")
scientific_week.add_participant("Stephen", "May 15")
scientific_week.add_participant("Sarah", "May 15")
scientific_week.add_participant("John", "May 16")
scientific_week.add_participant("Jennifer", "May 16")
scientific_week.get_participant_count()