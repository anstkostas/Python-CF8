# Σε αυτή την υλοποίηση αντί για match..case χρησιμοποιώ λεξικό ώστε να μπορώ να εξαντλήσω πιο εύκολα όλα τα error_codes.
def get_http_error(error_code):
    """
    Returns the HTTP error message corresponding to the given error code.
    
    Args:
      error_code (int): The HTTP error code.
    
    Returns:
      str: The corresponding error message.
    """
    
    error_messages = { # dictionary
        200: "OK",
        400: "Bad request",
        404: "Not found"
    }
    
    # Αυτό σε σύντμηση βρίσκεται παρακάτω. 
    # if not error_code in error_messages.keys():
    #   return "Unknown error"

    return error_messages.get(error_code, "Unknown error")

def main():
    error_code = 404
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()
