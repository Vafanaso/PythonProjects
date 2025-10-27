def rebase(input_base, digits, output_base):
    # --- Validate bases ---
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    # --- Handle edge case: empty input ---
    # --- Validate digits ---
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    # --- Convert input digits to an integer (base 10) ---
    number = 0
    for d in digits:
        number = number * input_base + d
    # --- Handle zero ---
    if number == 0:
        return [0]
    # --- Convert integer to output base digits ---
    result = []
    while number > 0:
        number, remainder = divmod(number, output_base)
        result.insert(0, remainder)
    return result
