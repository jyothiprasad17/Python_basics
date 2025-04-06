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
a,b=0,1
number=int(input())
for i in range(0,number):
    print(a)
    a,b=b,a+b

lets say input is 11 the o/p is
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



