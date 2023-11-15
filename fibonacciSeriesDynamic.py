def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result

# Example usage:
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
