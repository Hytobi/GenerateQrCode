import pyqrcode

# Put the link here
site = "https://github.com/Hytobi"

# Create the QR code
qr = pyqrcode.create(site)

# Save the QR code as a png file, change the name of the file
qr.png('gitcode.png', scale=6, module_color=[0, 0, 0, 128], background=[255, 255, 255])