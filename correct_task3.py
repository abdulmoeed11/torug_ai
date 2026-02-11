from typing import List, Union, Optional

def average_valid_measurements(values: List[Union[float, int, str, None]]) -> float:
    """
    Calculates the average of valid numeric measurements from a list.
    
    Valid measurements are defined as:
    - Non-None values
    - Values that can be successfully converted to a float
    
    Args:
        values: A list of candidate measurement values (can be int, float, str, or None).
        
    Returns:
        float: The average of the valid measurements. Returns 0.0 if no valid measurements exist.
    """
    if not values:
        return 0.0
        
    total = 0.0
    valid_count = 0
    
    for v in values:
        if v is None:
            continue
            
        try:
            # Try to convert to float. This handles ints, floats, and numeric strings.
            val = float(v)
            total += val
            valid_count += 1
        except (ValueError, TypeError):
            # Skip values that cannot be converted to a number
            continue
            
    if valid_count == 0:
        return 0.0
        
    return total / valid_count

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([], 0.0), # Empty input
        ([10, 20, 30], 20.0), # Simple valid case
        ([10, None, 30], 20.0), # Contains None (should be skipped)
        ([10, "20", 30], 20.0), # Contains string number
        ([10, "invalid", 30], 20.0), # Contains invalid string (should be skipped)
        ([None, None], 0.0), # All None
        (["invalid", "abc"], 0.0), # No valid numbers
        ([10, 20.5, "30.5"], 20.333333333333332), # Mixed types
    ]
    
    for inputs, expected in test_cases:
        result = average_valid_measurements(inputs)
        # Check equality with a small epsilon for float comparison
        passed = abs(result - expected) < 1e-9
        print(f"Input: {inputs} -> Expected: {expected}, Got: {result} ({'PASS' if passed else 'FAIL'})")
