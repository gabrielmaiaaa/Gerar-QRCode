import qrcode

# data = "url"
data = ""

qr = qrcode.QRCode(version=5, box_size=50, border=4)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png");