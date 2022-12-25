import pyqrcode

NomReseau = "MonReseauWiFi"  # Put your wifi name here
TypeSecurite = "WPA"
MotDePasse = "MonMotDePasseWiFi" # Put your wifi password here

# Generate the QR code
qr = pyqrcode.create("WIFI:S:{NomReseau};T:{TypeSecurite};P:{MotDePasse};;")

# Save the QR code as a PNG file
qr.png('wificode.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
