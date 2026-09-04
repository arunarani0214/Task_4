#Task 3

#question 1 Eligibility for Admission 
Mark1, Mark2, Mark3 = map(int,input('Enter your marks').split(','))

print(((Mark1 >80)and (Mark2 >80) and (Mark3>80)) and ('Elligible')or('Not Elligible'))



#question 2 Employee's bonus
Experience =input('Enter Employee experience')
Experience = int(Experience )
Rating = input('Ratings')
Rating = int(Rating)
Salary =50000

print((Experience>=5 and Rating>=4) and (Salary + (Salary*0.5)) or 'No increment')


#question 3
Purchase_amount = int(input('Enter Purchase Amount'))
Membership_status = input('Membership status')

if (Membership_status=='yes'):

 if (Purchase_amount<5000):
    Discount = (Purchase_amount * 10)/100
    print('Your discount is',Discount )
 elif ((Purchase_amount>=5000)and(Purchase_amount<10000)):
    Discount = (Purchase_amount * 20)/100
    print('Your discount is',Discount)
  
else:
  print('you are not eligible for this offer')
  Discount = False 
Membership_discount = Purchase_amount - Discount
print(Membership_discount)
Festival_offer = (Membership_discount*10)/100
Final_payment = Membership_discount-Festival_offer
print('Final Payment',Final_payment)


#question 4
import random
Signup_username = input('Enter Username for setup')
Signup_password = int(input('Enter Password for setup'))

Signin_username = input('Enter Username for signin')
Signin_password = int(input('Enter password for signin'))

if((Signup_username == Signin_username) and (Signup_password == Signin_password)):
   otp = random.randint(0000,9999)
   otp = int(otp)
   print(otp)
   otp1 = int(input('Enter your otp'))
   if (otp1 == otp):
       print('Logged in successfully')
   else:
       print('Incorrect otp')

else:
   print('Incorrect username or password')      


#question 5 ATM 
Withdrawal_amount = int(input('Enter the withdrawal amount'))
Account_balance = int(10000)
Min_balance = int(5000)


if((Withdrawal_amount>= Min_balance) and (Withdrawal_amount%100 == 0)):
   
   Amount = Account_balance - Withdrawal_amount
   print(Amount)
   if(Amount>= 100):
      print('Processing your request....')
      print('You can withdraw only', Amount)
else:
   print('your request cant be processed')




#question 6

a = ['Aruna','Ashok','Navi', 'Nakul']
b = 'Navi'

print(b in a)

Sentence = 'You are kind'
print('kind' in Sentence)

c = input('Enter your list')
d = input('Enter your word')

print(d in c)

#question 7

A = int(input('Enter your number'))
Start_range, End_range=map(int,input('Enter your range').split(','))

if ((A>= Start_range)and (A<=End_range)) and (A%3==0) or (A%5==0):
   print('Number is within the range and divisible by either 3 or 5')
else:
   print('Not in the Range')









