from itertools import permutations
digits = input("Enter 3 digits (e.g., 123): ")
if len(digits) != 3 or not digits.isdigit():
    print("Please enter exactly 3 digits.")
else:
    digit_permutations = permutations(digits)
    print("All possible combinations:")
    for perm in digit_permutations:
        print(''.join(perm))
