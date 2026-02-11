# AI Code Review Assignment (Python)

## Candidate
- Name:Abdul Moeed
- Approximate time spent: 50 mins

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- **Division by Zero**: If the `orders` list is empty, `len(orders)` is 0, causing a `ZeroDivisionError` on the return line.
- **Incorrect Logic**: The code calculates the average by dividing the sum of *non-cancelled* amounts by the *total count of all orders* (including cancelled ones). This incorrectly dilutes the average. It should divide by the count of *valid* orders only.

### Edge cases & risks
- **KeyError**: If an order dictionary is missing the keys `"status"` or `"amount"`, the code will crash.
- **TypeError**: If `"amount"` is not a number (e.g., `None` or a string), the addition operation will fail.
- **All Cancelled Orders**: If all orders are cancelled, the corrected logic would have a valid count of 0, which also needs to be handled to avoid division by zero.

### Code quality / design issues
- **Missing Type Hinting**: Function arguments and return types are not annotated.
- **Missing Docstring**: No documentation explaining expected input format or return value.
- **Fragile Logic**: Implicit assumptions about dictionary structure make the code brittle. 

## 2) Proposed Fixes / Improvements
### Summary of changes
- Implement a check for empty input list.
- Count only valid (non-cancelled) orders for the divisor.
- Add safeguards for missing keys and invalid types.
- Handle the case where no valid orders exist (avoid division by zero).
- Add docstrings and type hinting.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
1. **Empty List**: Ensure it returns 0.0 without error.
2. **All Cancelled**: Ensure it returns 0.0 and doesn't divide by zero.
3. **Missing Keys**: Test with dictionaries missing "status" or "amount" to verify robustness.
4. **Invalid Amount Types**: Test with strings or None for amounts.
5. **Mixed Valid/Invalid**: Verify expected calculation logic (sum of valid amounts / count of valid orders).


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation claims the function "correctly excludes cancelled orders from the calculation," which is misleading. While it excluded them from the numerator (sum), it included them in the denominator (count), resulting in an incorrect average.

### Rewritten explanation
- This function calculates the average order value by summing the amounts of all orders where the status is not 'cancelled' and dividing by the count of those specific valid orders. It safely handles empty inputs, missing keys, and cases where no valid orders exist. 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
  **Request Changes**
- Justification:
  The critical division by zero bug and the logical error in average calculation make the current implementation incorrect and unsafe for production.
- Confidence & unknowns:
  High confidence. The logic flaw is evident from basic arithmetic principles (average = sum of items / count of items). However, there are still some unknowns about the expected behavior in edge cases such as spelling mistakes or casing inconsistencies in status or amount or cancelled values.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- **Incorrect Validation Logic**: The condition `if "@" in email` is insufficient. It counts any string containing an `"@"` symbol (e.g., `"@"`, `"user@@"`, `"invalid_email@"`) as valid, failing to enforce standard email structure (username, domain, top-level domain).
- **TypeError on Non-String Input**: If the `emails` list contains non-string elements (e.g., integers, `None`), the check `if "@" in email` raises a `TypeError`. The function crashes instead of skipping invalid types.

### Edge cases & risks
- **Structural Integrity**: Emails missing a username (`"@domain.com"`), a domain (`"user@"`), or a TLD (`"user@domain"`) are incorrectly counted as valid.
- **Multiple @ Symbols**: Strings like `"user@sub@domain.com"` are counted as valid despite breaking standard format rules.
- **Whitespace Handling**: The function does not trim whitespace, meaning invalid entries like `" user@domain.com "` (with spaces) are accepted without sanitization, assuming strict validation is required.

### Code quality / design issues
- **Missing Type Hinting**: Function arguments and return types are not annotated.
- **Missing Docstring**: No explanation of validation criteria or return value.
- **Fragile Implementation**: Relying on a single character check for complex validation logic is poor practice. 

## 2) Proposed Fixes / Improvements
### Summary of changes
- Replaced simple `"@"` check with a regular expression (regex) to enforce `username@domain.tld` structure.
- Added type checking `isinstance(email, str)` to safely skip non-string inputs.
- improved robustness against empty input and invalid formats.
- Added comprehensive type hinting and a docstring. 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
1. **Invalid Structures**: Test missing username, missing domain, missing TLD (e.g., `"user@.com"`, `"@domain.com"`, `"user@domain"`).
2. **Special Characters**: Verify behavior with multiple `@` symbols, spaces, or forbidden characters.
3. **Non-String Input**: Pass a list containing integers, `None`, or other objects to ensure it doesn't crash.
4. **Valid Emails**: Ensure standard formats (e.g., `user.name@domain.co.uk`) are correctly identified.
5. **Empty List**: Confirm it returns 0 for empty input.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The explanation claims the function "safely ignores invalid entries," which is incorrect; encountering a non-string entry (like `None` or an int) causes a crash.
- It states that it handles validation correctly, but checking only for `"@"` is factually insufficient for email validation. 

### Rewritten explanation
- This function counts the number of valid email addresses in the input list by verifying they match a standard email pattern (username@domain.tld) using regular expressions. It safely handles mixed data types by skipping non-string entries and returns the count of strictly valid emails. 

## 4) Final Judgment
- Decision: Approve / **Request Changes** / Reject
- Justification:
  The original code lacks basic validation logic (checking only for `@`) and crashes on invalid input types, making it unsuitable for production use.
- Confidence & unknowns:
  High confidence. Email validation is a standard problem with well-defined structural rules that the original code completely ignores. The regex implemented covers the majority of standard use cases.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- **Incorrect Average Logic**: The code divides the sum of *valid* measurements by the total count of *all* elements (including `None` values). This results in an incorrect, diluted average. It should divide by the count of valid measurements only.
- **Division by Zero**: If the input list `values` is empty, `len(values)` is 0, causing a `ZeroDivisionError` on the return line.
- **Crash on Invalid Types**: The function assumes any non-None value can be converted to a float. If the list contains non-numeric strings (e.g., `"unknown"`), `float(v)` raises a `ValueError` or `TypeError`, causing the program to crash.

### Edge cases & risks
- **All None Values**: If the list contains only `None` values, `total` is 0 but `count` is positive. The function returns 0.0, which is mathematically "safe" but logically potentially misleading if the intent was to signal "no data". However, if we fix the logic to divide by valid count, an "all None" list yields a valid count of 0, risking division by zero again.
- **Mixed Types**: The code handles mixed valid types (integers, strings that look like numbers) implicitly, but fails on invalid strings.

### Code quality / design issues
- **Missing Type Hinting**: No type hints for the input list or return value.
- **Missing Docstring**: No documentation explaining what constitutes a "valid" measurement.
- **Silent Failures**: The current implementation might return a value (incorrectly calculated) even when significant data handling errors (like including `None` in the denominator) are occurring. 

## 2) Proposed Fixes / Improvements
### Summary of changes
- Modified logic to divide the sum by the count of *valid* measurements only.
- Added a check for empty input or no valid measurements to avoid `ZeroDivisionError`.
- Added a `try-except` block to safely handle values that cannot be converted to float (e.g., "N/A", "error"), skipping them instead of crashing.
- Added type hinting and docstrings. 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
1. **Empty Input**: ensure it returns 0.0 without error.
2. **All None/Invalid**: Ensure it handles lists with no valid numbers gracefully (returns 0.0).
3. **Dilution Logic**: Check `[10, None]` to ensure the result is `10.0` (10/1), not `5.0` (10/2).
4. **Crash Prevention**: Pass non-numeric strings like `"cannot_parse"` to verify it doesn't crash.
5. **Mixed Valid Types**: Verify `[10, "20.0"]` correctly sums to 30.0.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The explanation states it "safely handles mixed input types," which is false; it crashes on non-numeric strings.
- It implies accurate averaging, but the logic incorrectly includes `None` values in the denominator count.

### Rewritten explanation
- This function calculates the average of valid numeric measurements from a list. It filters out `None` values and non-numeric strings, ensuring that the average is calculated based solely on the count of successfully parsed numbers. It safely handles empty inputs and mixed data types. 

## 4) Final Judgment
- Decision: Approve / **Request Changes** / Reject
- Justification:
  The original function calculates the average incorrectly (logic error) and is prone to crashing on invalid input (runtime error).
- Confidence & unknowns:
  High confidence. The logic error is mathematically provable, and the runtime error is easily reproducible.
