import hashlib
import os
import datetime

# Function to generate a random salt
def generate_salt():
    return os.urandom(16)  # Generates 32 bytes of random data

# Function to hash the password with a salt
def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

def user_exists(username):
    try:
        with open('passwd.txt', 'r') as file:
            for line in file:
                record_username, _, _, _, _ = line.strip().split(',')
                if record_username == username:
                    return True
    except FileNotFoundError:
        # If the file doesn't exist, we can assume the user doesn't exist either
        return False
    return False

# Function to add a record to the password file
def add_record(username, password, role):
    if user_exists(username):
        return False, "User ID is already taken."

    salt = generate_salt()
    hashed_password = hash_password(password, salt)  # This should return a bytes object
    timestamp = datetime.datetime.now().isoformat()

    try:
        with open('passwd.txt', 'a') as file:
            # Ensure hashed_password is a bytes object before calling .hex()
            file.write(f"{username},{hashed_password.hex()},{salt.hex()},{role},{timestamp}\n")
        return True, "User successfully enrolled."
    except Exception as e:  # Catch any exception to ensure a tuple is returned
        return False, f"Failed to write to password file: {e}"
    
# Function to retrieve a record from the password file
def get_record(username):
    with open('passwd.txt', 'r') as file:
        for line in file:
            record_username, _, _, _, _ = line.strip().split(',')
            if record_username == username:
                return line.strip()
    return None

# Example usage of add_record and get_record
if __name__ == "__main__":
    # Add multiple user records
    user_info = [
        ('johndoe', 'password123', 'System Administrator'),
        ('janedoe', 'password456', 'Finance Manager'),
        ('mikebrown', 'password789', 'Auditor'),
        ('sarahsmith', 'pass123', 'Teller')
    ]

    for username, password, role in user_info:
        add_record(username, password, role)
        print(f"Record added for {username}.")

    print("\nRetrieving and displaying all added records:")
    # Retrieve and print the added records
    for username, _, _ in user_info:
        record = get_record(username)
        print(f"Record for {username}: {record}")