# Task 2
#Question 1 postive, nagative or zero
a = int(input('Enter the number'))
if (a>0):
   print('Positive Number')
elif (a<0):
   print('Negative Number')
else:
   print('Its Zero')


#question 2
b = int(input('Enter your number'))
if (b%2==0):
  print('Its Even number')
else:
  print('Odd number')
'''
'''
#question  3
c = int(input('Enter your number'))
if (c%3==0)and(c%5==0):
    print('Its divisible by both 3 and 5')
elif (c%3==0)and(c%5!=0):
    print('Divisible by only 3')
elif (c%3!=0)and(c%5==0):
    print('Divisible by only 5')
else:
    print('Not divisible by 3 and 5')



#question 4 Electricity bill
unit_consumed = int(input('Enter the units consumed'))

if (unit_consumed>0) and (unit_consumed<=100):
  print('Amount =',(unit_consumed*2))
elif (unit_consumed>=101) and (unit_consumed<=200):
 print('Amount = ',(unit_consumed*3))
elif (unit_consumed>=201) and (unit_consumed<=300):
 print('Amount =',(unit_consumed*5))
else:
 print('Amount =',(unit_consumed*7))


#question 5 Multiplication table
a = int(input('Enter any number'))

for i in range (1,21):
    print(i,'*',a,'=',(i*a))



#question 7 Pattern program

for i in range (1,6):
  for j in range (i):
     print('*',end= " ")
  print()
    


#question 10 Leap year or not
year = int(input('Enter the year'))

if (year%4==0 and year %100 !=0) or(year %400==0):
  print(year, 'is a leap year')
else:
  print(year,'is not a leap year')


#question 11 min and max
a,b,c = map(int,input('Enter three numbers').split(','))

if (a>b)and(a>c):
  print(a, 'is  maximum amoung threee numbers')
elif (b>c) and (b>a):
  print(b,'is maximum amoung three numbers')
else:
  print(c,'is maximum amoung three numbers')

if (a<b) and (a<c):
  print(a,'is min amoung three numbers')
elif (b<c) and (b<a):
  print(b,'is min amoung three numbers')
else: 
  print(c,'is min amoung three numbers')


  
  











  

























