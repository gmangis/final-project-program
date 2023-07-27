# user_management.py

def register_user(name, age, gender, username, password):
    # Implement user registration logic here
    # Validate input and store user data

    def login_user(username, password):
    # Implement user login logic here
    # Validate input and check credentials
    # Return True if login is successful, otherwise False

        def is_valid_username(username):
    # Function to validate the username
    # Implement validation logic here (e.g., alphanumeric characters)
            return username.isalnum()

def is_valid_password(password):
    # Function to validate the password strength
    # Implement validation logic here (e.g., minimum length, complexity requirements)
    return len(password) >= 8
