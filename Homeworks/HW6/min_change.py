'''
Name: Dylan Phoutthavong
Date: May 8th, 2025
Course: CSCI 3412
Task(s): Write a Python program to find a solution for any specified amount.
'''

def get_minimal_change(amount):
    # Convert to cents to avoid floating point issues
    cents = int(round(amount * 100))
    
    denominations = {
        "$100": 10000,
        "$50": 5000,
        "$20": 2000,
        "$10": 1000,
        "$5": 500,
        "$1": 100,
        "50¢": 50,
        "25¢": 25,
        "10¢": 10,
        "5¢": 5,
        "1¢": 1
    }

    change = {}
    for name, value in denominations.items():
        count = cents // value
        if count:
            change[name] = count
            cents -= count * value

    return change

# Example usage:
amount = 269.63
result = get_minimal_change(amount)
print(f"Minimal change for ${amount}:")
for denom, count in result.items():
    print(f"{denom}: {count}")