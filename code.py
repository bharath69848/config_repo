def check_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = 10
result = check_odd_or_even(num)
print(f"The number {num} is {result}.")