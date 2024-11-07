import math

def calculate_c(x):
    try:
        numerator = math.sqrt(math.log(2) + math.log(x))
        denominator = math.pow(math.tan(x), 1/3) + math.sqrt(math.pow(math.cos(x), 4))
        c = math.tan(abs(x)) - numerator / denominator
        return c
    except ValueError as e:
        return f"Error: {e}"

x = 1
result = calculate_c(x)
print("Результат:", result)
