def validate_password(password):
    """
    Validates a password based on specified requirements.
    
    Args:
        password (str): The password to validate
        
    Returns:
        dict: A validation result containing:
            - 'valid' (bool): Whether the password is valid
            - 'errors' (list): List of validation error messages
    """
    errors = []
    
    # Check minimum length requirement
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    
    # Check for at least 2 numbers
    if sum(1 for char in password if char.isdigit()) < 2:
        errors.append("The password must contain at least 2 numbers")
    
    # Check for at least one capital letter
    if not any(char.isupper() for char in password):
        errors.append("password must contain at least one capital letter")
    
    # Check for at least one special character
    if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password):
        errors.append("password must contain at least one special character")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'error_message': '\n'.join(errors) if errors else None
    }