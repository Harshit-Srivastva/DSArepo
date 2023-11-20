def mod_exp(base, exponent, modulus):
    result = 1

    base = base % modulus  # Take modulus of base to handle large base values

    while exponent > 0:
        # If exponent is odd, multiply result with base
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # exponent must be even now
        exponent = exponent // 2
        base = (base * base) % modulus

    return result

# Example usage:
base = 2
exponent = 10
modulus = 1000000007

result = mod_exp(base, exponent, modulus)

print(f"{base}^{exponent} mod {modulus} = {result}")
