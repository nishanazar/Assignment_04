from pyzbar.pyzbar import decode

from PIL import Image

img = Image.open("F:/Generative_AI_Course/Python_class\Assignments_4/Assignments 01/Project_3_QR_code_encoder_decoder_Python_Project/myqrcode2.png")

result = decode(img)

print(result)