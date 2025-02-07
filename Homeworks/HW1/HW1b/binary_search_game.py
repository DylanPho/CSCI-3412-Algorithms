'''
Name: Dylan Phoutthavong
Date: January 28th, 2025
Course: CSCI 3412
Task(s): 1. Your program generates a random integer number between 1 and 1,000.  
           Then it uses the famous binary search algorithm to automatically guess the generated random number.   
           For each try, count the number of guesses to guess the random number correctly.  
         
         2. Repeat the previous step 10,000 times.  Then compute the average number of guesses out of 10,000 tries.
         
         3. Repeat the previous two steps with random numbers between 1 and 1,000,000 instead of 1,000 (max number)

'''

import random

def binary_search(low, high, target):
    '''
    Binary search function to find the target number
    Returns the number of guesses required to find the target
    '''
    guesses = 0 # Counter for the number of guesses
    while low <= high:
        guesses += 1 # Increment guess count
        mid = (low + high) // 2 # Calculate the middle point
        if mid == target: # Check if mid  is the target
            return guesses
        elif mid < target: # If mid is less than target, search in the upper half
            low = mid + 1
        else: # If mid is greater than target, search in lower half
            high = mid - 1
    return guesses

def search_simulation(max_num, trials):
    '''
    Function to simulate binary seach, repeating 
    max_num: the maximum number in the range (1 to max_num)
    trials: the number of trials to perform
    Return total guesses and average guesses
    '''
    total_guesses = 0 # Initialize total guess count
    for _ in range(trials):
        target = random.randint(1, max_num) # Generate a random target number
        total_guesses += binary_search(1, max_num, target) # Perform binary srarch and accumulate guesses
        average_guesses = total_guesses / trials # Calculate average guesses
        return total_guesses, average_guesses
    
def main():
    '''
    Main Funciton
    '''
    # Simulation for numbers between 1 and 1,000
    total_guesses_1k, avg_guesses_1k =  search_simulation(1000, 10000)
    print(f"1. The random numbers between 1 .. 1K: Total guesses: {total_guesses_1k}, Avg: {avg_guesses_1k:.5}")

    # Simulation for numbers between 1 and 1,000,000
    total_guesses_1m, avg_guesses_1m =  search_simulation(1000000, 10000)
    print(f"2. The random numbers between 1 .. 1M: Total guesses: {total_guesses_1m}, Avg: {avg_guesses_1m:.5}\n")

main()