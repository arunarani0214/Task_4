from PIL import Image #Python Imaging Library
import stepic
import pywhatkit


# Encode
img = Image.open(r"D:\parrot.png")

password = "0000"
message = "Hiii"

#Data to hide
data_to_hide = password + "|" + message

encoded = stepic.encode(img, data_to_hide.encode())
encoded.save(r"D:\ar.png")


 print("Saved!")


# Auto send via WhatsApp
pywhatkit.sendwhats_image("+919600476155", r"D:\ar.png", "Check this image", 15, True, 2)
