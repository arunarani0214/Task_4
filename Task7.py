#1.Fibonacci series and factorial using Function
def factorial(a):
    b =1
    for i in range(1,a+1):
        b = b*i
    print(b)    
factorial(5)

def fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

fibo(10)


#2.Find the length of a string
def length(string):
   print("Length of a given string is...",len(string))
    
string = input("Enter any string...")
length(string)

#3.Find the maximum value of the number
def max_value(b):
    print("Maximum value in the given List is ...",max(b)) 

a = int(input("Range..."))
b = []
for i in range(0,a):
    c = input("Enter the elements..")
    b.append(c)
print(b)
max_value(b)    
   

#4.Find the minimum value of the number
def min_value(a):
    print("Minimum value in the given Tuple is ...",min(a))

a = int(input("Enter the range of a Tuple..."))
b =[]
for i in range(0,a):
     c = int(input("Enter the Tuple Elements..."))
     b.append(c)
print(tuple(b))
min_value(b)

        
#5.Find the sum of the number
def sum_1(a):
    b = 0
    for i in a:
        b = i+b
    print("Sum..",b)    
       
        
a = [1,2,3,4]
sum_1(a)


#6.Factorial using recursion function
def recursion(a):
    if a ==0 or a==1:
        return 1
    else:
        return (a*recursion(a-1))
print(recursion(5))    


#7.Write a function student_details(name, roll, dept) that prints the details using positional arguments.
def student_details(name,roll,dept):
    print(f"{name},{roll} is studying in {dept}...")

for i in range(0,2):
    name = input("Enter student name..")
    roll = int(input("Roll No.."))
    dept = input("Dept..")
    student_details(name,roll,dept)
               


#8.Write a function calculate_total(marks1, marks2, marks3) to calculate the total marks of a student using positional.
def calculate_total(mark1, mark2, mark3):
    total = mark1+mark2+mark3
    print("Total is ",total)

mark1,mark2,mark3 = map(int,input("Enter marks..").split())
calculate_total(mark1,mark2,mark3)


#9.Write a function rectangle_area(length, width) that calculates the area of a rectangle using positional argument.
def rectangle_area(length,width):
    area = length*width
    print("Area of Rectangle ",area)

l = int(input("length "))
w = int(input("Width "))        
rectangle_area(l,w)



#10.Write a function greet_user(name, message="Good Morning") that prints a greeting using default argument.
def greet_user(name, message="Good Morning"):
    print(f"{name},{message}")
    print(name,message)
greet_user("Navi")


#11.Write a function add_numbers(*args) that returns the sum of any number of values.
def add(*args):
    a = int(input())
    b = int(input())
    c = a+b
    return c

print(add())

#12.Write a function multiply_all(*args) that multiplies any number of values.
def multiply(*num):
    total = 1
    for i in num:
        total = total*i
    return total

print(multiply(1,2,20))


#13.Write a function to add two numbers.
def add(a,b):
    c = a+b
    return c
a,b = map(int,input("Enter two numbers...").split())
print("Addition of two numbers is ",add(a,b))



#14.Write a function to find the square of a number.
def square(a):
    a = a*a
    return a

a = int(input("Enter any number.."))
print("Square of ",a," is ",square(a))
        



#15.Write a function to check whether a number is even or odd.
def check(a):
    if a%2 == 0:
        print(f"{a} is a Even number")
    else:
        print(f"{a} is a Odd number")

a = int(input("Enter a number"))
check(a)
        
#16.Write a function to find the maximum of two numbers.
def maximum(a,b):
    if a>b:
        return a
    else:
        return b

a,b = map(int,input("Enter two numbers...").split())
result = maximum(a,b)
print(f"{result} is maximum")

#17.Write a function to find the factorial of a number.
def factorial(a):
    b = 1
    for i in range(1,a+1):
        b = b*i
    return b

a = int(input("Enter any number..."))
result = factorial(a)    
print(f"Factorial of a given number is {result}")        




















