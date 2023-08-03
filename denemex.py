import qrcode

data = "https://www.youtube.com/watch?v=IIm_pxD8Csk"
filename = "yxx_code.png"

qr = qrcode.QRCode(
    version=1 ,
    error_correction=qrcode.constants.ERROR_CORRECT_L , 
    box_size= 10 , 
    border= 4 ,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "black" , back_color = "white")
img.save(filename)

print("QR KOD BAŞARIYLA OLUŞTURULDU!!")