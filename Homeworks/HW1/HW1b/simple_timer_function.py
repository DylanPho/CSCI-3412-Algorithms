'''
Name: Dylan Phoutthavong
Date: January 28th, 2025
Course: CSCI 3412
Task(s): 1. Write a function, "timeEfficiency(funcName, *args, **kwargs)" :
          - The timeEfficiency() function takes two input arguments, a function (funcName) and a list of arguments of the function. 
           Then it executes the specified function with the specified arguments.
          - Prints out 1) start time, 2) end time, and then 3) total time to execute the specified function
         
         2. To test the timeEfficiency() function, you also write a test function listPrimeNumbers(theMaxNum), which takes an integer 
         (theMaxNum) and lists all prime numbers between 0 and theMaxNum sent to the function. Feel free to get the code from the Internet.
         
         3. Next, write a test driver which asks the user to enter a number to be passed to listPrimeNumbers() function.  The test driver calls 
         timeEfficiency() function with the arguments of listPrimeNumbers() function and theMaxNum to measure the time efficiency of listPrimeNumbers() function.

'''

import time

def timeEfficiency(funcName, *args, **kwargs):
    '''
    Function to measure the time efficeiency of a given function
    funcName: The function that will be timed
    *args: Positional arguments to pass to funcName
    **kwargs: Keyword arguments to pass to funcName
    '''
    start_time = time.perf_counter() # Record the start time
    result = funcName(*args, **kwargs) # Call the function with provided arguments
    end_time = time.perf_counter() # Record the end time

    # Calculate total execution time
    total_time = end_time - start_time

    # Print timing details
    print(f"\n'Start': {start_time:.5f}, 'End': {end_time:.5f}, 'Time Efficiency': {total_time:.5f}")

    return result

def listPrimeNumbers(theMaxNum):
    '''
    Function to list all prime numbers up to theMaxNum
    theMaxNum: The upper limit for generating prime numbers
    '''
    primes = [] # List to store prime numbers

    # Check all numbers from 2 to theMaxNum
    for num in range(2, theMaxNum + 1):
        is_prime = True # Assume the number is prime

        # Check divisibility by all smaller numbers
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False # Number is not prime
                break

        if is_prime:
            primes.append(num) # Add prime number to the list

    return primes

def main():
    '''
    Main function
    Promt the user to test the above functionality 
    '''
    try:
        theMaxnum = int(input("Enter a number for the list of prime numbers: "))
        if theMaxnum < 2:
            print("Please enter a number greater than or equal to 2.")
            return
        
        # Measure the time efficiency of the listPrimeNUmbers function
        primes = timeEfficiency(listPrimeNumbers, theMaxnum)

        # Print the result
        print(f"List of prime numbers up to {theMaxnum}: {primes}")

    except ValueError:
        print("Invalid input. Please enter an integer.")

main()