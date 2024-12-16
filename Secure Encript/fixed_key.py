from cryptography.fernet import Fernet

# Generate and print a valid Fernet key
key = Fernet.generate_key()
print(key.decode())  # Use this key in your application
