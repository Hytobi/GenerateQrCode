import pyqrcode

import pyqrcode

# Créer une chaîne vCard pour les informations de contact suivantes :

# Start
Svcard = "BEGIN:VCARD\n"
Svcard += "VERSION:4.0\n"

# - Nom complet : John Smith
Svcard += "FN:John Smith\n"

# - Nom de famille : Smith, Prénom : John
Svcard += "N:Smith;John;;;\n"

# - Adresse email : john.smith@example.com
Svcard += "EMAIL:john.smith@example.com\n"

# - Numéro de téléphone : +1 555 555 5555
Svcard += "TEL:+1 555 555 5555\n"

# - Organisation : Acme Inc.
Svcard += "ORG:Acme Inc.\n"

# - Titre : President
Svcard += "TITLE:President\n"

# - Rôle : Manager
Svcard += "ROLE:Manager\n"

# - Photo : https://www.example.com/john_smith.jpg
Svcard += "PHOTO;VALUE=URL:https://www.example.com/john_smith.jpg\n"

# - Adresse postale : 123 Main Street, Anytown, US, 12345
Svcard += "ADR:123 Main Street;Anytown;US;12345\n"

# - Site web : http://www.acme.com
Svcard += "URL:http://www.acme.com\n"


# - Notes : This is a note about John Smith.
Svcard += "NOTE:This is a note about John Smith.\n"


# - Date d'anniversaire : 1970-09-01
Svcard += "BDAY:19700901\n"


# - Date de dernière modification : 2022-12-25 19:52:43
Svcard += "REV:20221225T195243Z\n"


# - Identifiant unique : abcdefghijklmnopqrstuvwxyz
Svcard += "UID:abcdefghijklmnopqrstuvwxyz\n"

# End
Svcard += "END:VCARD"

# Créer un QR code à partir de la chaîne vCard
qr = pyqrcode.create(Svcard)

# Enregistrer le QR code dans un fichier image
qr.png("qr_code_vcard.png", scale=8)
