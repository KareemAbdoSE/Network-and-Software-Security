# password_checker.py

import re

# Assuming this set will be updated or replaced by a dynamic source in production
COMMON_WEAK_PASSWORDS = {
    "Password1", "Qwerty123", "12345678", "!@#$%^&*", "password", "user1234", "admin", "Finvest123"
}

def is_valid_password(password, user_id):
    if len(password) < 8 or len(password) > 12:
        return False, "Password must be 8-12 characters long."
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    
    if not re.search(r"[!@#$%?\*]", password):
        return False, "Password must contain at least one special character from {!@#$%?*}."

    if password in COMMON_WEAK_PASSWORDS or user_id.lower() in password.lower():
        return False, "Password is too common, weak, or contains the user ID."

    # Check for patterns resembling dates, license plates, telephone numbers
    if re.search(r"(19|20)\d\d[- /.]?(0[1-9]|1[0-2])[- /.]?(0[1-9]|[12][0-9]|3[01])", password):
        return False, "Password must not resemble a date."
    
    # Add any other pattern checks needed...

    return True, "Password is valid."

# Example usage
if __name__ == "__main__":
    test_password = "ValidPass!9"
    test_user_id = "user123"
    validity, message = is_valid_password(test_password, test_user_id)
    print(f"Password Validity: {validity}, Message: {message}")
