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
    
    return {
        'valid': len(errors) == 0,
        'errors': errors
    }