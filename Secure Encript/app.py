from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Use your fixed key here
key = b'Cs6DZo_EFcA3YROFcBt-wlFGXhqQ6IPYfxIrmjurs8E='  # Your fixed key
cipher = Fernet(key)

# In-memory storage for messages
messages = []

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Get the encrypted message from the request
        encrypted_message = request.json['message']
        # Store the encrypted message
        messages.append(encrypted_message)
        return jsonify({"status": "Message stored successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_message', methods=['GET'])
def get_message():
    if not messages:
        return jsonify({"error": "No messages found"}), 404
    
    # Decrypt the last stored message
    decrypted_message = cipher.decrypt(messages[-1].encode()).decode()
    return jsonify({"message": decrypted_message}), 200

if __name__ == '__main__':
    app.run(debug=True)
