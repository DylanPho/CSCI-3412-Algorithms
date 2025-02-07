'''
Name: Dylan Phoutthavong
Date: February 4th, 2025
Course: CSCI 3412
Task(s): Re-implement timeEfficiency() function using decorators and test it with the listPrimeNumber program.  
(NOTE: You need to submit both implementations of timeEfficiency() functions - the initial basic one and the decorator one)

'''

import time

def timeEfficiency_decorator(func):
    """
    Decorator to measure the time efficiency of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Record the start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.perf_counter()  # Record the end time

        # Calculate total execution time
        total_time = end_time - start_time

        # Print timing details
        print(f"\n'Start': {start_time:.5f}, 'End': {end_time:.5f}, 'Time Efficiency': {total_time:.5f}")
        return result
    return wrapper

@timeEfficiency_decorator
def listPrimeNumbers(theMaxNum):
    """
    Function to list all prime numbers up to theMaxNum.
    """
    primes = []
    for num in range(2, theMaxNum + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Main Function
def main():
    try:
        theMaxNum = int(input("Enter a number for the list of prime numbers: "))
        if theMaxNum < 2:
            print("Please enter a number greater than or equal to 2.")
            return

        # Measure time efficiency using the decorator
        primes = listPrimeNumbers(theMaxNum)

        # Print the result
        print(f"List of prime numbers up to {theMaxNum}: {primes}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

main()
