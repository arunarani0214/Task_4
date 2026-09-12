'''
#1.Check if a number is positive, negative, or zero.
a = int(input("Enter any number .."))

if a>0:
    print(a, " is a Positive integer")
elif a<0:
    print(a, " is a Negative integer")
else:
    print(a,",is Zero")
'''
'''
#2.Find the largest of three numbers.
a,b,c =map( int,(input("Enter 3 numbers...")).split(','))

if (a>b)and(a>c):
    print(a,"a is the largest of 3")
elif (b>a)and(b>c):
    print(b,"b is the largest of 3")
else:
    print(c," is the largest of 3")
'''

'''
#3.Print the multiplication table of a given number.
a = int(input("Enter the table you want..."))

for i in range(1,21):
    b = a*i
    print(a , "*" , i,"=",b)
'''
'''
#4.Check if a year is a leap year.
year = int(input("Enter any year..."))

if (year%4 == 0):
    if (year%100 !=0) or (year%400 ==0):
        print(year,"is a Leap Year")
    else:
        print(year,"is not a Leap Year")
'''
'''
#5.Write a program to check if a student has passed (marks ≥ 40).
Math,EVS,Eng = map(int,input("Enter the marks..").split(','))

if (Math>=40)and (EVS>=40)and(Eng>=40):
     print("Pass")
else:
    print("Fail")
'''
'''
#6.Keep asking the user for a password until they enter the correct one.
Actual_password = "Navi123"

while 1:
     password = input("Enter your password...")
     if password == Actual_password:
         print("Logged in successfully...")
         break
     else:
         print("Incorrect password")
'''         
'''
#7.Print the first 10 Fibonacci numbers.
n=int(input("enter any number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
'''        
'''  
#8.Print numbers from 1 to 20, but skip multiples of 3.    
a = int(input("Enter any number..."))

for i in range (a):
    if (i%3 != 0):
      print(i)
'''
'''
#9.Find the factorial of a number using a loop.
#a = int(input("Enter any number..."))
a = 1
for i in range (1,6):
     a = i*a
print(a)
'''

'''
#10.Count how many even numbers are between 1 and 50.
a = 0
for i in range (1,51):
    if(i%2 == 0):
        a +=1
print(a)   
'''
'''
#11.Count vowels and consonants in a string.
a = input("Enter a string....")
vowels = 0
consonents = 0
for i in range (len(a)):
    
    if a[i] in "aeiouAEIOU":
        print("Vowels")
        vowels += 1
    else:
        print("Consonents")
        consonents +=1


print(vowels)
print(consonents)

'''
'''
#12.Reverse a string without using slicing.
string = "Nakul"

for i in range(len(string)-1,-1,-1):
    string1 = string[i]
    print(string1)
'''
'''
#13.Check if a string is a palindrome.
string = "noon"
string1 = ""
for i in range(len(string)-1,-1,-1):
    string1 += string[i]
    
print(string1)
if string == string1:
        print(string," is Palindrome")
else:
        print(string," is not Palindrome")
'''
'''
#14.Count how many times a particular word appears in a sentence.
a = "Navi Nakul Nakul"
b = a.split()
print(b)
count = 0
word = "Nakul"

for i in b:
   if i == word:
       count+=1

print(count)
'''
'''
#15.Find the longest word in a sentence.
a = "Navi Navilan Nakul"
b = a.split()
print(b)
long =""

for i in b:
    if len(i)>len(long):
      long = i

print(long)
print(len(long))
'''
'''
#16.Replace spaces in a string with hyphens.
a = "Navi Nakul Navilan"
print(a.replace(" ","-"))
'''
'''
#17.Count digits, letters, and special characters in a string.

string = input("Enter string: ")
digit = 0
alp = 0
spec = 0
for i in string:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        alp += 1
    else:
        spec += 1
print("Digits count =  ", digit)
print("Letters count = ", alp)
print("Special =  ", spec)
'''
'''
#18.Find the largest and smallest number in a list.
a=[10,2,3,4,5]
print(max(a))

'''
'''
#19.Remove duplicates from a list.
a = [1,1,2,2,3,3,4,4]
b = list(set(a))
print(b)
'''
'''
#20.Calculate the sum and average of numbers in a list.
a = [1,2,3]
b = [2,3,4]
c = a+b
print(c)

a = [1,2,3]
b = sum(a)
c = sum(a)/len(a)
print(b)
print(c)

'''
'''
#21.Sort a list in ascending and descending order.
a = [5,4,6,2,3]
a.sort()
print("Ascending order",a)
b = a[::-1]
print("Decending order",b)
a.reverse()
print("Decending order",a)
'''
'''
#22.Create a list of cubes for numbers 1–10.
b =[]

for i in range(1,11) :
    i = i**3
    print(i)
    b.append(i)
print(b)
'''
'''
#23.Find the second largest number in a list.
a =[1,2,3,4,5]
b = 0


for i in a:
    if i <max(a) and i>b:
        b = i
print(b)       
'''
'''
#24.Merge two lists into one.
a = [1,2,3]
b = [4,5]
a.extend(b)
print(a)
'''
'''
#25.Access the 2nd and 4th elements of a tuple.
a = (1,2,3,4,5)
print(a[1])
print(a[3])
'''
'''
#26.Check if an element exists in a tuple.
a = (1,2,3,4,5)
b = int(input("Enter any number"))

if b in a:
    print(b,"is present in the given Tuple")
else:
    print(b,"is not present in the given Tuple")
    
'''
'''
#27.Convert a tuple into a list and back into a tuple.
a = (1,2,3,4,5)
print(list(a))
print(tuple(a))

'''
'''
#28.Find the length, maximum, and minimum in a tuple.
a = (1,2,3,4,5)
print(len(a))
print(min(a))
print(max(a))

'''
#29.Concatenate two tuples.

a = (1,2)
b = (3,4)
c = a+b
print(c)















































































    























































































































































    
