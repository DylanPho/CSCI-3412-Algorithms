'''
Name: Dylan Phoutthavong
Date: February 4th, 2025
Course: CSCI 3412
Task(s): 1) Write a code executing the following:

            a) First, randomly generate three numbers [0..9] (***The order among three numbers matters***)

            b) Then, continuously guess all three numbers until all three are guessed correctly.  See below for two different ways of guessing three random numbers.

            c) Keep track of the number of guesses for the three random numbers

            d) Repeat the steps a) - c) x number of times in an outer loop, where x should be equal to or larger than 10,0000

            e) Compute the average of guesses per try computed from x number of tries.

'''

import random
import itertools

def deterministic_brute_force(target):
    '''
    Determine brute-force algorithm to guess three random numbers
    '''
    guesses = 0
    for perm in itertools.permutations(range(10), 3): # Generate all permutations of 3 numbers
        guesses += 1
        if list(perm) == target:
            return guesses
    return guesses

def pure_random_guess(target, max_tries = 10000):
    '''
    Random guessing algorithm to guess three random numbers
    '''
    guesses = 0
    while guesses < max_tries:
        guesses += 1
        guess = [random.randint(0, 9) for _ in range(3)] # Generate a random guess
        if guess ==  target:
            return guesses
    return -1 # To show that max tries were exceeded

def guessing_simulation(algorithm, num_tries, max_tries = 10000):
    '''
    Simulation function to calculate average guesses for a given algorithm
    '''
    total_guesses = 0
    max_guesses = 0
    min_guesses = float('inf')
    bailed_out_cases = 0

    for _ in range(num_tries):
        target = [random.randint(0, 9) for _ in range(3)] # Generate a random target
        guesses =  algorithm(target) if algorithm == deterministic_brute_force else algorithm(target, max_tries)

        if guesses == -1: # Handle baled-out cases to make algorithm output random
            bailed_out_cases += 1
            continue

        total_guesses += guesses
        max_guesses = max(max_guesses, guesses)
        min_guesses = min(min_guesses, guesses)

    average_guesses = total_guesses / (num_tries - bailed_out_cases) if num_tries != bailed_out_cases else 0
    return total_guesses, average_guesses, max_guesses, min_guesses, bailed_out_cases

def main():
    '''
    Main Function
    '''
    num_tries = 10000  # Number of trials to perform

    # Run deterministic brute-force algorithm
    print("\nDeterministic brute-force guessing algorithm:")
    total_guesses, avg_guesses, max_guesses, min_guesses, _ = guessing_simulation(deterministic_brute_force, num_tries)
    print(f"Number of Tries: {num_tries}")
    print(f"The highest number of guesses in a try: {max_guesses}")
    print(f"The lowest number of tries: {min_guesses}")
    print(f"The average number of tries: {avg_guesses:.2f}\n")

    # Run pure random guessing algorithm
    print("Pure random guessing algorithm:")
    total_guesses, avg_guesses, max_guesses, min_guesses, bailed_out_cases = guessing_simulation(pure_random_guess, num_tries)
    print(f"Number of Tries: {num_tries}")
    print(f"The highest number of guesses in a try: {max_guesses}")
    print(f"The lowest number of tries: {min_guesses}")
    print(f"The average number of tries: {avg_guesses:.2f}")
    print(f"Number of bailed-out cases: {bailed_out_cases}")

main()