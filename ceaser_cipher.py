def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice not in ['e', 'd']:
        print("Invalid option. Please choose 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print(f"\n🔒 Encrypted message: {encrypted}")
    else:
        decrypted = caesar_decrypt(message, shift)
        print(f"\n🔓 Decrypted message: {decrypted}")

if _name_ == "_main_":
    main()
