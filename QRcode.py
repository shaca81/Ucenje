from qrcode import *

qr = QRCode(
    version=5,
    error_correction=ERROR_CORRECT_L,
    box_size=20,
    border=2)
qr.add_data("http://www.prelistavanje.org/")
qr.make()  # Generate the QRCode itself
#  im contains a PIL.Image.Image object
image = qr.make_image()  # To save it
image.save("filename.png")
qr.clear()
