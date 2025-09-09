import os
import json
from cryptography.fernet import Fernet

# Define the root directory for all user data
MEMORY_DIR = "user_memories"
# Define subdirectories
JSON_SUBDIR = "json_files"
IMAGES_SUBDIR = "images"

# --- Fernet Encryption Key Management ---
# It's crucial to have a single, securely stored key for all encryption/decryption.
# This is a simple example. In a production bot, you'd store this key in
# an environment variable or a secure key management system.
ENCRYPTION_KEY_FILE = "encryption_key.key"

def load_or_generate_key():
    """
    Loads the encryption key from a file or generates a new one if it doesn't exist.
    """
    if os.path.exists(ENCRYPTION_KEY_FILE):
        with open(ENCRYPTION_KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(ENCRYPTION_KEY_FILE, "wb") as key_file:
            key_file.write(key)
        return key

# Load the encryption key once when the bot starts
ENCRYPTION_KEY = load_or_generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

# --- User Data Paths (from your original code) ---

def get_user_data_path(user_id):
    """Gets the path to a user's JSON data file."""
    user_data_path = os.path.join(MEMORY_DIR, JSON_SUBDIR, f"{user_id}.json")
    os.makedirs(os.path.dirname(user_data_path), exist_ok=True)
    return user_data_path

# --- Encrypted Read/Write Functions ---

def save_encrypted_user_data(user_id, data):
    """
    Saves user data as an encrypted JSON file.
    Args:
        user_id (str): The Discord user ID.
        data (dict): The data to save.
    """
    file_path = get_user_data_path(user_id)
    
    # 1. Convert the dictionary to a JSON string
    json_string = json.dumps(data)
    
    # 2. Encode the string to bytes (Fernet works with bytes)
    data_bytes = json_string.encode('utf-8')
    
    # 3. Encrypt the bytes
    encrypted_data = cipher_suite.encrypt(data_bytes)
    
    # 4. Save the encrypted bytes to the file
    with open(file_path, "wb") as f:
        f.write(encrypted_data)

def load_encrypted_user_data(user_id):
    """
    Loads and decrypts user data from a JSON file.
    Returns:
        dict: The decrypted user data, or an empty dictionary if the file doesn't exist.
    """
    file_path = get_user_data_path(user_id)
    
    if not os.path.exists(file_path):
        return {} # Return an empty dictionary if no data exists for the user
    
    # 1. Read the encrypted bytes from the file
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
        
    try:
        # 2. Decrypt the bytes
        decrypted_bytes = cipher_suite.decrypt(encrypted_data)
        
        # 3. Decode the bytes back to a string
        json_string = decrypted_bytes.decode('utf-8')
        
        # 4. Convert the JSON string back to a dictionary
        return json.loads(json_string)
        
    except Exception as e:
        print(f"Error decrypting data for user {user_id}: {e}")
        # In a real bot, you might want to log this error and handle it gracefully
        return {}


# --- Example Usage ---

if __name__ == "__main__":
    test_user_id = "123456789"
    
    # Data to save
    user_memory = {
        "name": "Alice",
        "last_message_time": "2025-09-09T15:15:00Z",
        "bot_conversations": [
            "Hi, what's your name?",
            "My name is Alice."
        ]
    }
    
    print(f"Saving encrypted data for user {test_user_id}...")
    save_encrypted_user_data(test_user_id, user_memory)
    
    print("Attempting to load and decrypt the data...")
    loaded_data = load_encrypted_user_data(test_user_id)
    
    print("Decrypted data:")
    print(loaded_data)
    
    # Verify that the loaded data is the same as the original
    assert loaded_data == user_memory
    print("\nData loaded and decrypted successfully!")
    
    # Check the file on disk to see the encrypted content
    with open(get_user_data_path(test_user_id), "rb") as f:
        encrypted_content = f.read()
        print("\nEncrypted content in file (looks like gibberish):")
        print(encrypted_content)

# as you could think the actual memories are not just dictionaries but json/bin files that also include the persona_data
