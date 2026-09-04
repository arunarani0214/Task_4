
#Task 1
#Question 1 Arithmetic Operations

A = int(input("Enter A value"))
B = int(input("Enter B value"))
print("Addition =",A+B)
print("Subtraction =",A-B)
print("Multiplication =",A*B)
print("Division =",A/B)
print("Remainder =",A%B)
print("Power =",A**B)
print("Floor Division =",A//B)        



#Question 2 Area and Perimeter
#for square
a = int(input("Enter the side value"))
Area = print(a**2)
Perimeter = print(4*a)

#for circle
r = int(input("Enter Radius"))
Area = print(3.14*(r**2))
Perimeter = print(2*3.14*r)

#for Rectangle
l = int(input("Enter length"))
b = int(input("Enter breadth"))
Area = print(l*b)
Perimeter = print(2*(l+b))


#Question 3 Average
a,b,c= map(int,input("Enter 3 numbers").split(','))
print("Avg of 3 numbers is",(a+b+c)/3)



#Question 4 Comparison
a = int(input("Enter a value"))
b = int(input("Enter b value"))

if a==b:
    print("Both are equal")
elif a>b:
    print("A is greater than B")
else:
    print("B is greater")


#Question 5 Square root
a = int(input("Enter a value"))
print("Square root of",a,"is",(a**0.5))


#Question 6 Simple and Compound Interest
P = int(input("Principal"))
R = int(input("Interest Rate"))        
T = int(input("No of years"))

Interest = (P*R*T)/100
print("Simple Interest",Interest)

N = int(input("No of years Interest is compounded"))
Compound = P*(1+R/100/N)**(N*T)
print("Compound Interest",Compound)


#Question 7
x = int(input("Enter x  "))
print("x = ",x)
x+=5
print("x+=5",x)
x-=3
print("x-=3",x)
x*=2
print("x*=2",x)
x/=4
print("x/=4",x)
x%=2
print("x%=2",x)
x**=3
print("x**=3",x)

# Question 8
A = int(input("Enter A"))
B = int(input("Enter B"))
A = A+B
B = A-B
A = A-B
print("Swapped A",A)
print("Swapped B",B)


#question 9
Username = 'Aruna'
Password = 'Aruna@123'
Username_1 = input('Enter username')
Password_1 = input('Enter password')


print((Username==Username_1)and (Password==Password_1) and 'Success'or 
'Fail')

A = (Username==Username_1) and (Password == Password_1)

if A==1:
 print('Logged in successfully')
else:
 print('Incorrect')


#question 10 Cube root
x = int(input('Enter a number'))
print('Cuberoot of',x,'is',(x**(1/3))










































































        
        
        

        

        
