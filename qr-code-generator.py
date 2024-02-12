# perfect applicationn to print QR codes for mass scans like onto cars or billboards or banners. and this method is totally free

import qrcode
from qrcode.exceptions import DataOverflowError
from PIL import Image
from datetime import datetime


def generate_qr_code(url, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=4,
                     fill_color="white", back_color="black", output_file="login_page_qr.png"):
    try:
        # init qrcode as an object
        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction,
            box_size=box_size,
            border=border,
        )

        # add data to qr code
        qr.add_data(url)

        # generate tge qr code image
        qr.make(fit=True)

        # create image from qr code
        qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)

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
        # if the file doesnt exist, set count to 0
        scan_count = 0

    scan_count += 1

    # save the count
    with open(file_path, "w") as file:
        file.write(str(scan_count))

    print(f"QR code scanned! Total scans: {scan_count}")


# test usage
login_page_url = "https://www.sunatasigns.co.za/" # any valid URL can be passed here.
generate_qr_code(login_page_url,
                 version=2,
                 box_size=10,
                 border=2,
                 fill_color="red",
                 back_color="black",
                 output_file="tester_qr_code.png")
track_qr_scans("qr_code_scans.txt")
