import qrcode
from qrcode.exceptions import DataOverflowError
from PIL import Image
import os

# List of URLs to cycle through
websites = {
    "aluma": "https://aluma.co.za/",
    "fintegrate": "https://fintegratetech.co.za/",
    "lndr": "https://onboarding.lndr.credit/broker/auth/login",
    "uatPortal": "https://uatportal.aluma.co.za/advisor/auth/login"
}

def generate_qr_code(url, logo_path, output_file):
    try:
        # init the QR code project
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=4,
        )

        # add data to QR code
        qr.add_data(url)

        # generate QR code image
        qr.make(fit=True)

        # create image from QRCode
        qr_image = qr.make_image(fill_color="darkblue", back_color="white")

        # open logo image
       # logo = Image.open(logo_path)

        # calculate logo size to fit into the QR code
       # qr_width, qr_height = qr_image.size
        #logo_width, logo_height = logo.size
       # logo_size = min(qr_width, qr_height) // 4

        # resize the logo
       # logo = logo.resize((logo_size, logo_size))

        # calculate the position to paste the loogo in the center of the QR code
        #position = ((qr_width - logo.width) // 2, (qr_height - logo.height) // 2)

        # paste the logo yo the QR code
        #qr_image.paste(logo, position)

        # save the image
        qr_image.save(output_file)

        print("QR code generated successfully!")
    except DataOverflowError:
        print("Data provided is too large to fit in the specified QR code version.")
    except Exception as e:
        print(f"An error occurred: {e}")

def track_qr_scans(file_path):
    try:
        with open(file_path, "r") as file:
            scan_count = int(file.read())
    except FileNotFoundError:
        # if the file doesnt exist set count to 0
        scan_count = 0

    scan_count += 1

    # save the count
    with open(file_path, "w") as file:
        file.write(str(scan_count))

    print(f"QR code scanned! Total scans: {scan_count}")

# create directory if it doesnt exist
output_directory = "qr_code"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# get logo path
logo_path = "logo.png"

# generate QR codes with logo
for label, url in websites.items():
    output_file = os.path.join(output_directory, f"{label}_qr_code.png")
    generate_qr_code(url, logo_path, output_file)

# track QR code scans
track_qr_scans("qr_code_scans.txt")
