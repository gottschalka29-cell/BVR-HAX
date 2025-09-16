# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
     
#     def say_info(self):
#         print("Your name is " + self.name + ". You are " + str(self.age))
    
#     def age_years(self, old):
#         for i in range(old):
#             print("Happy Birthday! You are turning " + str(self.age + i + 1)    )
#         self.age += old

# p = Person("John", 20)
# p.say_info()
# p.age_years(5)
# p.say_info()

# class Dog:
#     def __init__(self,name):
#         self.name = name
    
#         def play(self):
#             print("the dawg is played with a toy")    
        
#         def sleep(self):
#             print("The dog was sleeping" )
        
#         def day_cycle():
#             self.sleep()
#             self.play()
#             self.play()
#             self.play()
#             self.play()

# D =Dog("dawg")
# D.day_cycle()

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_perimeter(self):

        pass

    @abstractmethod 
    def get_area(self):
        pass

    def print_all_info(self):
        print("The perimeter is " + str(self.get_perimeter()) + (". The area is " + str(self.get_area())))

class Square(Shape):
    number = 4
    number2 = 4
    new_number = 0
    def get_perimeter(self):
        self.number += self.number2 *2
        return self.number
    def get_area(self):
        self.new_number = self.number * self.number2 
        return self.new_number
    

class Rectangle(Shape): 
    number = 2 
    number2 = 8
    new_number = 0
    def get_perimeter(self):
        self.number += self.number2 *2
        return self.number
    def get_area(self):
        self.new_number = self.number * self.number2 
        return self.new_number

class Triangle(Shape):
    number = 4
    new_number = 0 
    def get_perimeter(self):
        self.number * 3 
        return self.number
    def get_area(self):
        self.new_number = self.number + self.number / 2 
        return self.new_number
    
S = Square()
S.print_all_info()

r = Rectangle()
r.print_all_info()
t = Triangle()
t.print_all_info()