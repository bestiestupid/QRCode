import qrcode

image = qrcode.make("www.youtube.com")  # insert what you want ot make QR of
image.save("QRCode.jpg")
