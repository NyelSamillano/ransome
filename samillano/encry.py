from cryptography.fernet import Fernet
import os


def load_or_generate_key(key_file='C:/Users/alber/Documents/samillano/key.key'):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    return key


def encrypt_file(input_file_path, output_file_path, key):
    cipher_suite = Fernet(key)
    with open(input_file_path, 'rb') as f:
        data = f.read()
    encrypted_data = cipher_suite.encrypt(data)
    with open(output_file_path, 'wb') as f:
        f.write(encrypted_data)


def main():
    base_dir = 'C:/Users/alber/Documents/samillano/'
    data_dir = os.path.join(base_dir, 'file')

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    key = load_or_generate_key()

   
    input_text_files = ['bsit.txt', 'bsit2.txt']
    for input_text_file in input_text_files:
        input_text_path = os.path.join(data_dir, input_text_file)
        encrypted_text_path = os.path.join(data_dir, f'{os.path.splitext(input_text_file)[0]}_encrypted.txt')
        encrypt_file(input_text_path, encrypted_text_path, key)
        os.remove(input_text_path)

    image_files = ['ivan.jpg', 'ivana.jpg']
    for image_file in image_files:
        input_image_path = os.path.join(base_dir, image_file)
        encrypted_image_path = os.path.join(base_dir, f'{os.path.splitext(image_file)[0]}_encrypted.jpg')
        encrypt_file(input_image_path, encrypted_image_path, key)
        os.remove(input_image_path)

    print("Encryption completed.")

if __name__ == "__main__":
    main()
