n = int(input())

def use_ham_co_san(n):
    hex_number = hex(n)
    return hex_number[2:].upper()

def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEF"
    hex_number = ""
    
    while n > 0:
        remainder = n % 16
        hex_digit = hex_digits[remainder]
        hex_number = hex_digit + hex_number
        n = n // 16
    
    return hex_number

print(use_ham_co_san(n))