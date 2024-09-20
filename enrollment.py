# enrollment.py

from password_checker import is_valid_password
from password_manager import add_record, user_exists

def enroll_user(): 
    user_id = input("Enter User ID: ")
    # Check if the user ID already exists
    if user_exists(user_id):
        print("User ID already taken, please choose another.")
        return  # Exit the function if the user ID is taken

    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return  # Exit the function if the passwords do not match

    if user_id in password:
        print("Password must not contain the user ID. Please try again.")
        return  # Exit the function if the password contains the user ID

    valid, message = is_valid_password(password, user_id)
    if not valid:
        print(message)
        return  # Exit the function if the password is not valid

    role = input("Enter your role (e.g., Regular Client, Premium Client, Financial Advisor): ")
    if role not in ['Regular Client', 'Premium Client', 'Financial Advisor', 
                    'Financial Planner', 'Investment Analyst', 'Technical Support', 
                    'Teller', 'Compliance Officer']:
        print("Invalid role. Please enter a valid role.")
        return  # Exit the function if the role is not valid

    # Attempt to add the record and exit the function if it fails
    success, message = add_record(user_id, password, role)
    print(message)
    if not success:
        return  # Exit the function if adding the record failed

    print("User successfully enrolled.")
    # The function ends after successful enrollment

if __name__ == "__main__":
    enroll_user()
