# test_enrollment.py

import io
import sys
from unittest.mock import patch
from enrollment import enroll_user

def test_enroll_user():
    # Mock user_exists to always return False for testing purposes
    # Mock add_record to always return a success message
    test_user_data = [
        ("newuser", "NewPass!123", "NewPass!123", "Regular Client", "User successfully enrolled."),
        ("newuser1", "NewPass!123", "Mismatch123", "Passwords do not match."),
        # ... (other test cases)
    ]

    with patch('password_manager.user_exists', return_value=False), \
         patch('password_manager.add_record', return_value=(True, "User successfully enrolled.")):
        for user_data in test_user_data:
            with patch('builtins.input', side_effect=user_data[:-1]), \
                 patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
                enroll_user()
                output = fake_stdout.getvalue().strip()
                assert user_data[-1] in output, f"Test failed for {user_data}. Expected '{user_data[-1]}' in output."

    print("All enrollment tests passed!")

if __name__ == "__main__":
    test_enroll_user()
