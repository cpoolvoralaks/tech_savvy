# def square_plus_one(a):
#     result = a * a + 1
#     return result
#
# print(square_plus_one(2))
#
# def give_zhi_something(a, b):
# 	return a + b
#
# print(square_plus_one(2))
# print(give_zhi_something("apple" , "pen"))

# import math
# def quadratic (a, b, c):
#     x_1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
#     x_2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
#     return x_1, x_2
# print(quadratic(1, 2, -3))

# age = 3
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')

# nested conditionals

# if x = y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else
#         print('y is greater than x')

##BMI

import math
#
# x = float(input("Please enter weight "))
# print(type(x))
# y = float(input('Please enter height '))
# print(type(y))
# def BMI (x, y):
#     z_1 = (x/y**2)
#     return z_1
#
#
# if BMI(x, y) >= 30:
#     print('Obesity')
# elif 29.9 >= BMI(x, y) >= 25:
#     print('Overweight')
# elif 24.9 >= BMI(x, y) >= 18.5:
#     print('Normal weight')
# else:
#     print('underweight')

# def fab(n):
#     """
#     this function will return the nth Fabonacci number
#
#     """
#     if n ==1 or n ==2:
#         return 1
#     else:
#         return fab(n-2) + fab(n-1)
#
# for i in range(1, 10):
#     print("The {}th Fabonacci number is {}. ".format(i,fab(i)))

# sum = 0
# for i in range(1, 10):
#     print('in the {}th iteration, current i is {}. sum is {}.'.format((i),i, sum))
#     sum = sum + i**2
#     print('\t after adding square of i, the new sum is {}\n'.format(sum))
#
# print(sum)

# SUM OF NAME
# total_value = 0
# name = 'aob'
#
# for letter in name:
#     total_value = total_value + (ord(letter)-96)
#
# print('The value of name {} is {}.'.format(name, total_value))

##COUNTDOWN
# def countdown(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#     print('Blastoff!')
#
# countdown(5)

# team = "New England Patriots"
#
# print(len(team))
# letter = team[1]
# print(letter)
#
# print(team[0])
# print(team[len(team)-1])
#
# print(team[-1])
# print(team[-20])
#
# for letter in team:
#     print(letter)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)
#
# result = 0
# for number in range(1, 1001):
#     if number % 2 == 0:
#         result = result + number
#
# print(result)

team = 'New England Patriots'

print(team[0:11])
print(team[12:20])

print(team[12:])

name = 'anna'
def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome(name))

new_team = ""
for letter in team
    if letter != 'a':

print(new_team)