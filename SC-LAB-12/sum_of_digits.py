def sum_of_digits(n):
    """
    Recursive function to calculate the sum of digits of a number.
    
    Args:
        n (int): The input number (can be negative).
    
    Returns:
        int: The sum of the digits.
    """
    # Handle negative numbers by converting to positive
    n = abs(n)
    
    # Base case: if the number is 0, return 0
    if n == 0:
        return 0
    
    # Recursive case: sum the last digit and recurse on the remaining digits
    return n % 10 + sum_of_digits(n // 10)

if __name__ == "__main__":
    # Example test cases
    test_numbers = [0, 123, 987654321, -456, 999999999]
    for number in test_numbers:
        print(f"Sum of digits of {number}: {sum_of_digits(number)}")
