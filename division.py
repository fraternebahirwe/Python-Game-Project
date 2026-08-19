import re

def validate_credentials(email, password):
    """Validates the email and password.

    Args:
        email (str): Email address.
        password (str): Password.

    Returns:
        bool: True if valid, False otherwise.
    """

    # Validate email using regex
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    is_email_valid = re.match(email_regex, email)
    
    # Validate password (at least 8 characters)
    is_password_valid = len(password) >= 8
    
    return is_email_valid is not None and is_password_valid
# Test data
test_data = [
    ("test@example.com", "password123"),  # Valid
    ("invalid-email", "short"),            # Invalid email and short password
    ("user@domain.com", "1234567"),       # Valid email but short password
    ("user@domain.com", "validpass"),      # Valid email and password
    ("user@", "aValidPass123"),            # Invalid email
    ("@domain.com", "validPassword"),      # Invalid email
    ("user@domain.com", "pass"),           # Valid email but short password
    ("user&domain.com", "validpass123")    # Invalid email
]

# Testing the function
for email, password in test_data:
    result = validate_credentials(email, password)
    print(f"Email: {email}, Password: '{password}' -> Valid: {result}")
