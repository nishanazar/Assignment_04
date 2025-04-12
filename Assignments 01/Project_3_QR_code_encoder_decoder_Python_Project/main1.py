#   Qrcode
# Uses forword slash

import qrcode 

data = "Hello My name is Nisha Nazar"
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = "green", back_color = "white")


img.save("F:/Generative_AI_Course/Python_class\Assignments_4/Assignments 01/Project_3_QR_code_encoder_decoder_Python_Project/myqrcode2.png")