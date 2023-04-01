"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer：numerator or denominator is not numeric.
2. When will a ZeroDivisionError occur?
Answer: denominator equal 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

"""
function get_valid_denominator(prompt)
    get denominator
    while denominator==0:
        get denominator
    return denominator
    
get numerator
get denominator
fraction = numerator / denominator
print fraction
"""


def get_valid_denominator(prompt):
    denominator = int(input("Enter the denominator: "))
    while denominator==0:
        print("denominator can be zero!")
        denominator = int(input("Enter the denominator: "))

    return denominator

try:
    numerator = int(input("Enter the numerator: "))
    denominator = get_valid_denominator("Enter the denominator: ")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
