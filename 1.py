a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
limit = int(input("Enter the limit: "))

def sum_of_multiples(num1, num2, limit):
    total_sum = 0
    for i in range(1, limit):
        if i % num1 == 0 or i % num2 == 0:
            total_sum += i
    return total_sum


result = sum_of_multiples(a, b, limit)
print(f"The sum of multiples of {a} or {b} up to {limit} is {result}.")
