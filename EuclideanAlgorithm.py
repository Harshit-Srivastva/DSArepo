def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 48
num2 = 18

gcd_result = euclidean_gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {gcd_result}")
