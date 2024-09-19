# import qrcode

# def generate_qr_code(data, filename):
#     # Create a QR code object
#     qr = qrcode.QRCode(
#         version=1,  # controls the size of the QR Code
#         error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
#         box_size=10,  # controls how many pixels each “box” of the QR code is
#         border=4,  # controls how many boxes thick the border should be
#     )

#     # Add data to the QR code
#     qr.add_data(data)
#     qr.make(fit=True)

#     # Create an image from the QR code instance
#     img = qr.make_image(fill='black', back_color='white')

#     # Save the image
#     img.save(filename)
#     print(f"QR code generated and saved as {filename}")

# if __name__ == "__main__":
#     # Example usage
#     data = input("Enter the data to encode in the QR code: ")
#     filename = input("Enter the filename to save the QR code (e.g., qr_code.png): ")
#     generate_qr_code(data, filename)

