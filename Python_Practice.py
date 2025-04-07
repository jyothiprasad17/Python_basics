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

'''




