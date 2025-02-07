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

def collatz_sequence_length(n):
    """
    Generate the Collatz sequence for a given number and return its length and largest element.
    """
    length = 1
    largest = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        largest = max(largest, n)
        length += 1
    return length, largest

def analyze_collatz_sequence(range_limit):
    """
    Analyze the Collatz sequence lengths and largest values for numbers in the given range.
    """
    collatz_data = []  # List to store (starting_number, length, largest_element)

    for i in range(1, range_limit + 1):
        length, largest = collatz_sequence_length(i)
        collatz_data.append((i, length, largest))

    return collatz_data

def find_top_sequences(collatz_data, top_n=10):
    """
    Find the top N starting numbers with the longest Collatz sequences.
    """
    # Sort by sequence length in descending order
    collatz_data.sort(key=lambda x: x[1], reverse=True)
    return collatz_data[:top_n]

def main():
    '''
    Main Function
    '''
    range_limit = 10_000_000  # Define the range limit
    print("\nAnalyzing Collatz sequences...")

    # Analyze sequences
    collatz_data = analyze_collatz_sequence(range_limit)

    # Find the top 10 sequences
    top_sequences = find_top_sequences(collatz_data)

    # Display results
    print("Top 10 Collatz sequences:")
    for start, length, largest in top_sequences:
        print(f"Collatz sequence for {start}: {length} elements, largest element: {largest}")

main()
