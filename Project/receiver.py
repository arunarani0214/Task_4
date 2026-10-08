from PIL import Image #Python Imaging Library
import stepic
import pywhatkit

#Decode
decoded = stepic.decode(Image.open(r"D:\ar.png"))

saved_pass, saved_msg = decoded.split("|")

user_pass = input("Enter password: ")

if user_pass == saved_pass:
    print("Your secret is:", saved_msg)
else:
    print("Wrong password")


