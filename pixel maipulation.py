from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    encrypted_pixels = pixels ^ key
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    # Decryption is the same as encryption with XOR
    encrypt_image(image_path, key, output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? Enter E or D: ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice, please enter E or D.")
            continue

        image_path = input("Enter the path of the image file: ")
        try:
            key = int(input("Enter the encryption key (an integer): "))
        except ValueError:
            print("Invalid key, please enter an integer.")
            continue

        output_path = input("Enter the path for the output image file: ")

        if choice == 'E':
            encrypt_image(image_path, key, output_path)
        else:
            decrypt_image(image_path, key, output_path)

        again = input("Do you want to encrypt/decrypt another image? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
