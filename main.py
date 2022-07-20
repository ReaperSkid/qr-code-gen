import qrcode

QRCODEChoice = input("Your URL [-->]: ")

qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(QRCODEChoice)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')
