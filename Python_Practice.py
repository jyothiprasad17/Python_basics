'''# Converting a Integer into decimal
import decimal
i=10
print(decimal.Decimal(i))
print(type(decimal.Decimal(i)))

# Converting a string into decimal

s='12345'
print(decimal.Decimal(s))
print(type(decimal.Decimal(s)))

# Reversing a string using extended slicing technique

name='jyothi prasad'
print(name[::-1])

#counting vowels in a given word

vowels=['a','e','i','o','u','A','E','I','O','U']
name1=input()
count=0
for i in name1:
    if i in vowels:
        count +=1
print(count)

#counting Consonants in a given word

vowels=['a','e','i','o','u','A','E','I','O','U']
name2=input()
count=0
for i in name2:
    if i not in vowels:
        count = count+1
print(count)



# Counting of number of occurences of a character in a string

name_string=input()
character=input()
count=0
for i in name_string:
    if i==character:
        count=count+1
print(count)

'''

#Fibbabacio Number
'''a,b=0,1
l=[]
number=int(input())
for i in range(0,number):
    print(a)
    l.append(a)
    a,b=b,a+b
print(l)'''

'''lets say input is 11 the o/p is
0
1
1
2
3
5
8
13
21
34
55

here a,b=0,1
a,b = b,b+a ==>
0,1 = 1,1
1,1 = 1,2
1,2 = 2,3
2,3 = 3,5
3,5 = 5,8
5,8 = 8,13



#Finding Max Number in a list

l=list(input())
check = l[0]
for i in l:
    if check < i :
        check = i
print(check)

#Finding Min Number in a list

input_list=list(map(int, input().split(",")))
m =input_list[0]
for j in input_list:
    if m > j:
        m = j
print(m)

input() takes it as a string:
'1,4,5,11,6'

.split(',') splits the string by commas:
['1', '4', '5', '11', '6'] → This is a list of strings.

map(int, ...) applies the int() function to each element of the list:
map(int, ['1', '4', '5', '11', '6']) → turns it into: [1, 4, 5, 11, 6] → a list of integers.

list(...) converts the map object into a real list you can use.



# Middle Num of a list
number = [10, 25, 7, 43, 19,77]
print(int(len(number)/2))
middle = int(len(number)/2)
print(number[middle])



''''''# Converting a list into String
l=["P", "Y", "T", "H", "O", "N"]
s = "".join(l)
print(s)
print(type(s))
for i in l:
    print(i)

s = "".join(l)
This joins all elements of the list into a single string.

"".join(l) → uses an empty string as a separator.

# adding two lists

l1 = [11,12,13,14,15,16]
l2 = [21,22,23,24,25]
result=[]

result = l1+l2
print(result)



#Comparing two strings for ANAGRAM

str1="listen"
str2="silent"

str1.upper()
str2.upper()

if sorted(str1)==sorted(str2):
    print("Yes! str1 & str2 is ANAGARAM")
else:
    print("No Not a ANAGRAM")


#Checking for Palindrome using the extended slicing technique

name=input()
output = name[::-1]
if name ==output:
    print("It is a palindrome")
else:
    print("It is not a Palindrome")



# Counting white spaces in a string

name=input()
print(name.count(" "))



# Counting Letters, Digits and Spaces in a String


import re

name = input()

digit_count = re.sub("[^0-9]","",name)
Letter_count= re.sub("[^a-zA-Z]","",name)
Space_count= re.findall("[ \s]",name)

print(digit_count)
print(len(digit_count))
print(Letter_count)
print(len(Letter_count))
print(Space_count)
print(len(Space_count))



def special_character(text):
    sp_c="~!#$%^&*()`<>?:;'[]{}|\/"
    count=0
    for i in text:
        if i in sp_c:
            count=count+1
    print(count)

aa= special_character("hello world!@@@@!!@@@#@@*&(^(&(&)")
print(aa)


#Removing all white spaces in a string
import re
name = input()

space = re.compile(r'\s+')
output = re.sub(space,"",name)
print(output)


name1 = input("Provide any name with spaces:")
output1=name1.replace(" ","")
print(output1)



val=int(input())
for i in range(0,val):
    for j in range(i):
        print(" *",end=" ")
    print()


val = int(input())
for i in range(val):
    for j in range(val-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*", end ="")
    for j in range(i):
        print("*", end="")
    print()



val1=int(input())
for i in range(val1):
    for j in range(i):
        print(" * ",end="")

    print()
    


# Randomizing the items of a list in python

from random import shuffle

inputt=['adadfad','dfad','photon','uranium235']
shuffle(inputt)
print(inputt)

'''

'''def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True'''

#print(isprime(127))
'''Line-by-line Explanation:
1️⃣ def isprime(num):
This defines a function named isprime which takes one input argument num.

2️⃣ if num <= 1:
Prime numbers are greater than 1 (e.g., 2, 3, 5, 7...).

So if the input number is 0, 1, or negative, return False.

3️⃣ for i in range(2, num):
This loop checks every number i starting from 2 up to num - 1.

We’re checking: Does i divide num evenly?

4️⃣ if num % i == 0:
The % (modulo) operator checks for remainder.

If num % i == 0, then i is a factor of num, so num is not prime → return False.

5️⃣ return True (after the loop)
If we looped all the way from 2 to num-1 and found no divisors, the number is prime → return True.

🧪 Example with isprime(27):
27 > 1 → continue

Loop from 2 to 26:

27 % 2 ≠ 0

27 % 3 == 0 → divisible → not prime

So, the function returns False.

🔁 Summary of How It Works:
Input	Output	Why
2	True	Prime
4	False	Divisible by 2
5	True	Prime
27	False	Divisible by 3
-1	False	Not greater than 1'''

'''
def prime_generator(n):
    num=2
    while n:
        if isprime(num):
            yield num
            n = n-1
        num = num+1

prime = prime_generator(10)
for i in prime:
    print(i, end=",")

def prime_generator(n):
You're defining a generator function called prime_generator that takes one argument n — the number of prime numbers you want.

num = 2
Start checking from 2, because 2 is the first prime number.

while n:
This loop keeps running as long as n is not 0 — in other words, until you've found n prime numbers.

if isprime(num):
Here it checks whether the current num is a prime number using a helper function called isprime() 

yield num
🔑 This is the key part! Instead of return, you're using yield. This makes the function a generator — it remembers its state and can produce values one at a time in a loop, like:
    for p in prime_generator(5):
    print(p)
This will print 5 prime numbers one by one.

n = n - 1
After yielding a prime number, you decrease n by 1.

num = num + 1
Regardless of whether num was prime or not, you always increment it to check the next number.'''


'''def check_prime(x):
    if x <=1:
        return False
    for i in range(2,x):
        x%i == 0
        return True

print(check_prime(7))'''


#Implementing Variable lenght Arguments

'''def average(*t): # *t for tuple of variable length
    avg=sum(t)/len(t)
    return avg

print(average(1,4,4,2323,232,323231212,12))'''

'''def average_with_kwargs(**kwargs):
    values = list(kwargs.values())
    avg = sum(values)/len(values)
    return avg

print(average_with_kwargs(num=1, num2=4, num3=33))'''

# Creating Instance member variables in python

'''class Test:
    def __init__(self):
        self.a=47
    def f1(self):
        self.b=447

t1=Test()
t2=Test()

t1.f1()
t1.c=100

print(t1.__dict__)
print(t2.__dict__) # default values are observed as output when constructor __init__ is given'''


# Addition using Lambda Functions

'''f=lambda a,b : a+b
r=f(3,7)
print(r)

print((lambda a,b : a*b)(4,5))

print((lambda a : a*a)(4))'''

# Finding Factorial using Lambda functions

'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))


f=lambda n: 1 if n==0 else n*f(n-1)
print(f(3))'''

# List Compression ( To create a list in single line)

# list of even numbers
'''n=int(input())
l1 = [2*e for e in range(1,n)]
print(l1)

# to create a list of even numbers from a given list
l2 =[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 20, 92, 94, 96, 98, 100, 102, 104, 106, 108, 11, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198]
ll = [i for i in l2 if i%2==0]
print(ll)
 '''

#Split & Join condition
# split is to convert a string into a list of string.

'''s1 = "What is right in your mind is right in your world"
output = s1.split(" ")
print(output)
s2 = output[::-1]
print(s2)

# Join to convert list of string into string again

print("".join(s1))'''

# Global & Local Variable

'''x=5 # global variable

def fun1():
    global x
    x = 15 # global variable updated
    y = 10 # local variable
    print("x=%d y=%d" %(x,y))
#It's printing the values of variables x and y using old-style string formatting (also known as % formatting) in Python.

#🧩 Explanation:
#"x=%d y=%d" is a format string.
#%d is a placeholder for an integer (the "d" stands for decimal).
#%(x, y) is the tuple of values to insert into the placeholders.
print(fun1())
print(x)'''

# Globals Function

'''x = 5

def fun():
    x = 10 # local Variable
    d = globals() # d is a dictionary
    d['x']=15
    print( "local x=%d  global x=%d" %(x,d['x']))

print(fun())'''


# Python Decorator

# Function Decorator

'''def welcome(fx):
    def mfx(*t,**d):
        print("Before hello function")
        fx(*t,**d)
        print("Thanks for using the function")
    return mfx'''

'''What is a decorator in Python?
A decorator is a function that modifies or enhances another function without changing its actual code.
It’s like adding extra toppings on a pizza 🍕— the base remains the same, but you add new flavors on top.'''
'''def welcome(fx):                   # This is your decorator
    def mfx(*t, **d):              # Wrapper function: accepts any arguments (*t = tuple, **d = dict)
        print("Before hello function")
        fx(*t, **d)                # Call the original function (passed as fx)
        print("Thanks for using the function")
    return mfx                    # Return the modified version


@welcome
def hello(name):
    print(f"hello,{name}")

print(hello('jyothi prasad'))
@welcome → This applies the welcome decorator to hello.

It wraps hello inside mfx, adding behavior before and after the original function.

@welcome
def add(a,b):
    print(a+b)

print(add(5,6))
'''

#Class Decorator

'''class Calculator:

    def __init__(self, func):
        self.function=func

    def __call__(self, *t, **d):
        result = self.function(*t, **d)
        return result**2

@Calculator
def add(a,b):
    return (a+b)

print(add(10,20))
'''

# Iterators in Python

'''An iterator is an object in Python that allows you to loop through a sequence, like a list, tuple, string, etc., one element at a time.
It has two main methods:
__iter__() – returns the iterator object itself.
__next__() – returns the next value and raises StopIteration when it’s done.'''


'''l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
it = iter(l1) #This creates an iterator object from the list using the built-in iter() function.
while True: # Starts an infinite loop — it'll keep going unless we explicitly break out of it.
    try:
        print(next(it)) #Calls next() on the iterator it. Prints the next item in the list each time it's called.
    except StopIteration: # When next() runs out of items, it raises a StopIteration exception.
        break #This is caught by except, and then the loop ends with break.
'''

# Generator
# A generator is a function that returns an iterator, but instead of returning all values at once, it yields them one at a time as needed

'''def even_num(n):
    i=1
    while i<=n:
        yield 2*i
        i=i+1

for e in even_num(10):
    print(e)'''

New Program
