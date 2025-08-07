# Helpers/AES_helper.py
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Configuración
KEY_SIZE = 32  # 256 bits para AES-256
IV_SIZE = 16   # 128 bits
SALT_SIZE = 16
ITERATIONS = 100_000

def _derive_key(password: str, salt: bytes) -> bytes:
    """Deriva una clave AES-256 a partir de una contraseña y un salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=ITERATIONS,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt(texto_plano: str, password: str) -> str:
    """Cifra un texto plano con AES-CBC usando una contraseña."""
    salt = os.urandom(SALT_SIZE)
    iv = os.urandom(IV_SIZE)
    key = _derive_key(password, salt)

    padder = padding.PKCS7(128).padder() # type: ignore
    padded_data = padder.update(texto_plano.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    # Concatenamos salt + iv + ciphertext y lo codificamos en base64
    return base64.b64encode(salt + iv + encrypted).decode()

def decrypt(texto_cifrado: str, password: str) -> str:
    """Descifra un texto cifrado con AES-CBC usando una contraseña."""
    decoded = base64.b64decode(texto_cifrado)
    salt = decoded[:SALT_SIZE]
    iv = decoded[SALT_SIZE:SALT_SIZE+IV_SIZE]
    ciphertext = decoded[SALT_SIZE+IV_SIZE:]

    key = _derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder() # type: ignore
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data.decode()

def encrypt_file(file_path: str, password: str):
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = os.urandom(SALT_SIZE)
    iv = os.urandom(IV_SIZE)
    key = _derive_key(password, salt)

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    with open(file_path + ".aes", 'wb') as f:
        f.write(salt + iv + ciphertext)

def decrypt_file(file_path: str, password: str, output_path: str):
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = data[:SALT_SIZE]
    iv = data[SALT_SIZE:SALT_SIZE+IV_SIZE]
    ciphertext = data[SALT_SIZE+IV_SIZE:]

    key = _derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted = unpadder.update(padded_data) + unpadder.finalize()

    with open(output_path, 'wb') as f:
        f.write(decrypted)
