#Task 4

#1.Upper case
a = input("Enter your Name : ")
print(a)
print(a.upper())

#2.Lower case
b = input("Enter any sentence")
print(b.lower())

#3.Capitalize
print(b.capitalize())

#4.Format function
details = "My name is {} and  age is {}....".format("Navi","6")
print(details)

#5. Index
c = input("Enter any sentence :  ")
print(c.index("a"))


#6.Finding position of a substring
print(c.find("are"))

#7.Ends with 'ing'
print(c.endswith("ing"))

#8. \t spacing
space = "Navi\tNakul"
print(space.expandtabs())
d = space.expandtabs()

#9. Encode and Decode
print("Actual Text  :",d)
Encode = d.encode("utf-8")
print("Encoded Text : ",Encode)
Decode = Encode.decode("utf-8")
print("Decoded Text : ",Decode)

#10. Only Digits
print(Decode.isdigit())

#11. Numeric
print(Decode.isnumeric())

#12. Alpha numeric
print(Decode.isalnum())

#13. ASCII
print(Decode.isascii())

#14. Only Alphabets
print(Decode.isalpha())







