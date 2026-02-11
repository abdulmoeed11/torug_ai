import re
from typing import List, Any

def count_valid_emails(emails: List[str]) -> int:
    """
    Counts the number of valid email addresses in a list.
    
    A valid email is defined roughly as:
    - Non-empty username (alphanumeric + some special chars)
    - @ symbol
    - Non-empty domain
    - . symbol
    - TLD of at least 2 characters

    Args:
        emails: A list of candidate email strings.
        
    Returns:
        int: The count of valid email addresses.
    """
    if not emails:
        return 0
    
    # Simple yet robust regex for general email validation
    # ^: Start of string
    # [a-zA-Z0-9._%+-]+: Username (at least one char)
    # @: Literal @
    # [a-zA-Z0-9.-]+: Domain name (at least one char)
    # \.: Literal dot
    # [a-zA-Z]{2,}: Top Level Domain (at least 2 chars)
    # $: End of string
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    pattern = re.compile(email_regex)
    
    valid_count = 0
    
    for email in emails:
        # Safety check: Ensure the item is a string
        if not isinstance(email, str):
            continue
            
        # Check if it matches the pattern
        if pattern.match(email):
            valid_count += 1
            
    return valid_count

if __name__ == "__main__":
    # Small test suite
    test_cases = [
        ([], 0),
        (["valid@example.com"], 1),
        (["invalid-email"], 0),
        (["missing@domain"], 0), # No TLD
        (["@missinguser.com"], 0),
        (["user@.com"], 0),  # Empty domain
        ([123, None, "user@domain.com"], 1), # Mixed types
        (["user@domain.com", "another.user@sub.domain.org"], 2),
        ([" user@domain.com "], 0), # Leading/trailing whitespace (strict)
    ]

    for inputs, expected in test_cases:
        result = count_valid_emails(inputs)
        print(f"Input: {inputs} -> Expected: {expected}, Got: {result} ({'PASS' if result == expected else 'FAIL'})")
