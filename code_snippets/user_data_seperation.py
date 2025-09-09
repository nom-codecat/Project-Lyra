import os

# Define the root directory for all user data
MEMORY_DIR = "user_memories"
# Define subdirectories
JSON_SUBDIR = "json_files"
IMAGES_SUBDIR = "images"

def get_user_data_path(user_id):
    """Gets the path to a user's JSON data file."""
    user_data_path = os.path.join(MEMORY_DIR, JSON_SUBDIR, f"{user_id}.json")
    os.makedirs(os.path.dirname(user_data_path), exist_ok=True)
    return user_data_path

def get_user_images_dir(user_id):
    """Gets the path to a user's image directory."""
    user_images_path = os.path.join(MEMORY_DIR, IMAGES_SUBDIR, str(user_id))
    os.makedirs(user_images_path, exist_ok=True)
    return user_images_path
