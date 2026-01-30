numbers = []

print("Enter 5 numbers:")
for i in range(5):
    number = float(input(f"Input a number {i+1}: "))
    numbers.append(number)

numbers.sort(reverse=True)

print("\nNumbers sorted from highest to lowest:")
print(numbers)