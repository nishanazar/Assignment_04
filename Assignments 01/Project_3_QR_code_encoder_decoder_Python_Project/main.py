#   Qrcode
# Uses forword slash

import qrcode 

data = "https://github.com/nishanazar?tab=repositories"

img = qrcode.make(data)
img.save("F:/Generative_AI_Course/Python_class\Assignments_4/Assignments 01/Project_3_QR_code_encoder_decoder_Python_Project/myqrcode1.png")