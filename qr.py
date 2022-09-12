from turtle import back
import qrcode
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data="www.w3schools.com"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="blck",back_color="white")
img.save('qr.png') 