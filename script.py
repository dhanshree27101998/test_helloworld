import os
from cryptography.fernet import Fernet

# Generate a key (this should be stored securely for real use cases)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Access the secret value (temporary for debugging)
my_secret = os.getenv('MY_SECRET')

# Encrypt the secret value
encrypted_secret = cipher_suite.encrypt(my_secret.encode())

# Print the encrypted secret value
print(f"Encrypted secret value: {encrypted_secret}")

# Decrypt the secret value (for demonstration purposes, generally avoid printing secrets)
decrypted_secret = cipher_suite.decrypt(encrypted_secret).decode()
print(f"Decrypted secret value: {decrypted_secret}")
