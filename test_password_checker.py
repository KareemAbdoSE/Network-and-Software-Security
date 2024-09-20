# test_password_system.py

import password_checker
import password_manager

def test_password_validation():
    print("Testing Password Validation...")

    # Test cases for password validation
    test_cases = [
        ("ValidPass!9", "user123", True),
        ("short", "user123", False),
        ("noSpecialChar123", "user123", False),
        ("Nouppercase!123", "user123", False),
        ("NOLOWERCASE!123", "user123", False),
        ("WeakPassword1", "user123", False),
        ("user123Password!", "user123", False),
        ("2021-01-01Password!", "user123", False),
    ]

    for password, user_id, expected in test_cases:
        valid, message = password_checker.is_valid_password(password, user_id)
        assert valid == expected, f"Failed: {password} - {message}"

    print("All password validation tests passed!")

def test_password_manager():
    print("Testing Password Manager...")

    # Assuming the 'passwd.txt' file is empty or in a known state before testing
    username = "testuser"
    password = "TestPass!9"

    # Test adding a new user
    added, message = password_manager.add_record(username, password, "Test Role")
    assert added, f"Failed to add user: {message}"

    # Test checking if the user exists
    exists = password_manager.user_exists(username)
    assert exists, "User should exist but was not found."

    # Test retrieving a user record
    record = password_manager.get_record(username)
    assert record is not None, "Failed to retrieve user record."

    # Test password verification
    from login import verify_password  # Import the function from the correct module
    correct_pass, message = verify_password(username, password)
    assert correct_pass, "Password verification failed."

    print("All password manager tests passed!")

if __name__ == "__main__":
    test_password_validation()
    test_password_manager()

