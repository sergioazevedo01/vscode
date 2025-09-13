import qrcode

# pip install qrcode Pillow
data = "Opa eu sou Arthur !"
img = qrcode.make(data)
img.save("qrcode_image.png")

