from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import json

secret_key = b'my-secret-key' 

def encrypt_data(data):
    iv = b'\x00' * 16  # Este debe ser un valor único por cifrado en producción
    cipher = Cipher(algorithms.AES(secret_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(json.dumps(data).encode()) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_data).decode()

def decrypt_data(encrypted_data):
    encrypted_data_bytes = base64.b64decode(encrypted_data)
    iv = encrypted_data_bytes[:16]
    cipher = Cipher(algorithms.AES(secret_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data_bytes[16:]) + decryptor.finalize()
    return json.loads(decrypted_data)
