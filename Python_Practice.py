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
'''
#counting Consonants in a given word

vowels=['a','e','i','o','u','A','E','I','O','U']
name2=input()
count=0
for i in name2:
    if i not in vowels:
        count = count+1
print(count)