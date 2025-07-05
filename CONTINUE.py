#WAP to claculate the sq. root of the number , demonstrate the use break and continue statement.
import math

num = [4, 9, -16, 25, 36, 49, 64, 81, 100, 121, 144]

for num in numbers:
    if num < 0:
        print(f"Skipping {num} as it's negative.")
        continue  # Skip negative numbers
    try:
        sqrt = math.sqrt(num)
        print(f"Square root of {num} is {sqrt:.2f}")
        if num > 100:
            print("Stopping at number greater than 100.")
            break  # Stop loop when number exceeds 100
    except Exception as e:
        print(f"An error occurred: {e}")
