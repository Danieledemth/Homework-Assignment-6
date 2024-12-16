from cryptography.fernet import Fernet

# Use your fixed key here
key = b'Cs6DZo_EFcA3YROFcBt-wlFGXhqQ6IPYfxIrmjurs8E='  # Your fixed key
cipher = Fernet(key)

# Encrypt your message
message = "Misis University is one of the best university in Russia. it is located in the heart of Moscow"
encrypted_message = cipher.encrypt(message.encode())
print(encrypted_message.decode())  # Copy this output for cURL usage
