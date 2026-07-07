def calculate_power(base, exponent):
    result = 1.0
    # Get absolute value of exponent to manage the loop iterations
    abs_exponent = abs(exponent)
    
    while abs_exponent > 0:
        result *= base
        abs_exponent -= 1
        
    # If the original exponent was negative, invert the final result
    if exponent < 0:
        return 1.0 / result
    return result

# Example Usage
base_num = 2
n_power = -3
print(f"{base_num} raised to the power of {n_power} is: {calculate_power(base_num, n_power)}")
# Output: 2 raised to the power of -3 is: 0.125
