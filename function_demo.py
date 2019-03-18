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

x = float(input("Please enter weight "))
print(type(x))
y = float(input('Please enter height '))
print(type(y))
def BMI (x, y):
    z_1 = (x/y**2)
    return z_1


if BMI(x, y) >= 30:
    print('Obesity')
elif 29.9 >= BMI(x, y) >= 25:
    print('Overweight')
elif 24.9 >= BMI(x, y) >= 18.5:
    print('Normal weight')
else:
    print('underweight')

