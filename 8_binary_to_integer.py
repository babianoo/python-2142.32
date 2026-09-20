def binary_to_int(binary_str: str) -> int:
    result = 0
    for bit in binary_str:
        result = result * 2
        if bit == '1':
            result += 1
    return result

# Example usage:
print(binary_to_int("1011"))   # Output: 11
print(binary_to_int("11010"))  # Output: 26
print(binary_to_int("0010"))   # Output: 2
