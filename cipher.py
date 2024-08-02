def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? Enter E or D: ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice, please enter E or D.")
            continue

        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value, please enter an integer.")
            continue

        if choice == 'E':
            result = encrypt(message, shift)
            print("Encrypted message:", result)
        else:
            result = decrypt(message, shift)
            print("Decrypted message:", result)

        again = input("Do you want to encrypt/decrypt another message? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
