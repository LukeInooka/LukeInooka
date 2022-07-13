#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
'''
first_num = input('give me two numbers between 1 and 100\nFirst number: ')
second_num = input('Second number: ')
nums = [first_num,second_num]
if first_num > second_num:
    print(nums)
else:
    print(nums[1],nums[0])
'''

''''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
'''
user_input = input(str('input a string pls'))
str1 = ""
for i in (user_input):
    print(i,str1)
    str1 = i + str1
    print(str1)
print(str1)
'''

'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
'''
num = int(input('give me a number between 1 and 12: '))
for i in range(1,13):
    total = num*i
    print(i,'x',num,'=',total)
'''

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
'''
table =[]
for a in range(1,13):
    for b in range(1,13):
        total = a*b
        # print(a,'x',b,'=',total)
        table.append(total)
    print(table)
    table.clear()
'''

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
'''
user_input = input('type in some random numbers but dont use commas or dots cos itll confuse me')
nums = user_input.split(' ')
count = len(nums)
total = 0
for i in nums:
    total = total + int(i)
mean = total/count
print(mean)
'''

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
'''
total = 1
for i in range(1,16):
    total = total * i
print(total)
'''

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''

'''
fib_nums = [1,]
last = 1
last2 = 0
for i in range(1, 21):
    total = last + last2
    fib_nums.append(total)
    last2 = last
    last = total
    print(total)
print(fib_nums)
'''


'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''

'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
even =[]
odd = []
for i in range(1,101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even,odd)

