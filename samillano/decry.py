from cryptography.fernet import Fernet
import os

def load_key(key_file='C:/Users/alber/Documents/samillano/key.key'):
    with open(key_file, 'rb') as f:
        key = f.read()
    return key

def decrypt_file(input_file_path, output_file_path, key):
    cipher_suite = Fernet(key)
    with open(input_file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file_path, 'wb') as f:
        f.write(decrypted_data)

def check_payment(payment_amount):
    user_payment = float(input("Please pay 500 pesos to get all the files: "))
    if user_payment >= payment_amount:
        print("Payment successful. Decrypting files.")
        return True
    else:
        print("Insufficient payment. Files cannot be decrypted.")
        return False

def main():
    base_dir = 'C:/Users/alber/Documents/samillano/'
    data_dir = os.path.join(base_dir, 'file')

    payment_amount = 3000

    key = load_key()

    if not check_payment(payment_amount):
        return

   
    encrypted_text_files = ['bsit_encrypted.txt', 'bsit2_encrypted.txt']
    for encrypted_text_file in encrypted_text_files:
        encrypted_text_path = os.path.join(data_dir, encrypted_text_file)
        decrypted_text_path = os.path.join(data_dir, encrypted_text_file.replace('_encrypted.txt', '.txt'))
        decrypt_file(encrypted_text_path, decrypted_text_path, key)
        os.remove(encrypted_text_path)

   
    image_files = ['ivan_encrypted.jpg', 'ivana_encrypted.jpg']
    for image_file in image_files:
        encrypted_image_path = os.path.join(base_dir, image_file)
        decrypted_image_path = os.path.join(base_dir, image_file.replace('_encrypted.jpg', '.jpg'))
        decrypt_file(encrypted_image_path, decrypted_image_path, key)
        os.remove(encrypted_image_path)

    print("Decryption completed.")

if __name__ == "__main__":
    main()
