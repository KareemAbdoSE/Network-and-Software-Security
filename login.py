import roles
import hashlib
from password_manager import get_record

# Function to hash the password with a salt using PBKDF2 HMAC SHA-256
def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

def verify_password(user_id, password):
    # Retrieve the user record
    user_record = get_record(user_id)
    if not user_record:
        return False, "User not found."

    # Unpack the stored user information
    _, stored_hash, salt, _, _ = user_record.split(',')

    # Convert the stored salt back to bytes
    salt = bytes.fromhex(salt)

    # Hash the entered password with the stored salt
    entered_hash = hash_password(password, salt)

    # Compare the entered hash with the stored hash
    if entered_hash.hex() == stored_hash:
        return True, "Login successful."
    else:
        return False, "Incorrect password."

def display_user_info(user_id):
    # Retrieve the user record
    user_record = get_record(user_id)
    if user_record:
        username, _, _, role, _ = user_record.split(',')

        # Display user information
        print(f"\nUser ID: {username}")
        print(f"Role: {role}")

        # Display access rights or permissions based on the role
        permissions = roles.get_permissions(role)
        print("Access Rights/Permissions:")
        for permission in permissions:
            print(f" - {permission}")
    else:
        print("User record not found.")

def login():
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")
    success, message = verify_password(user_id, password)
    print(message)

    if success:
        display_user_info(user_id)

if __name__ == "__main__":
    login()
