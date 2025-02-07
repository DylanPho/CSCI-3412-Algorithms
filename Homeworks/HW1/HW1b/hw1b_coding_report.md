#### Dylan Phoutthavong 
#### February 24th, 2025 
#### CSCI 3287 

# HW1b Coding Report 

###  Problem 1: Number Guessing Game Using Binary Search 
***Approach***

The goal of this program was to efficiently guess a randomly generated number using the binary 
search algorithm. The program was implemented in the following steps: 
1. ***Binary Search Algorithm***: 
- The _binary_search_ function takes a low and high range and iteratively calculates the 
midpoint. 
- Depending on whether the midpoint is less than, greater than, or equal to the 
target number, the search range is halved. 
2. ***Simulation***: 
- A random number is generated within the specified range (1 to 1,000 and 1 to 
1,000,000). 
- The binary search function is executed to find the target, and the number of 
guesses is recorded. 
3. ***Results***: 
- This process is repeated 10,000 times for each range to calculate the total and 
average number of guesses. 

***Optimizations***
- ***Efficient Calculation***: The binary search algorithm guarantees time complexity, making 
it naturally ideal for this task. 
- ***Avoided Redundant Computation***: Reused calculations such as midpoint calculation 
only when the range changed, reducing overhead. 

#### Reflection 
This program shows the power of divide-and-conquer algorithms for solving search problems efficiently. The results showed how increasing the range logarithmically impacts the average number of guesses. 
 
### Problem 2: Simple Timer Function 
***Approach***

This program aimed to measure the execution time of a function using Python's time module. It 
involved: 
1. ***_timeEfficiency_ Function***: 
- Recorded the start and end times of a function execution. 
- Calculated and displayed the total time. 
2. ***Prime Number Generation***: 
- Implemented _listPrimeNumbers_ to find all primes up to a given number using trial 
division. 
- Nested loops guarantee divisibility checks up to the square root of each number, improving efficiency. 
3. ***Driver Program***: 
- Asks the user to input a number. 
- Passed the input to the _timeEfficiency_ function along with _listPrimeNumbers_

***Optimizations***
- ***Efficient Prime Checks***: Checked divisibility only up to the square root of each number to reduce unnecessary iterations. 

***Reflection***

This task shows the importance of time profiling in algorithm development. The implementation 
of timeEfficiency can be reused for performance analysis of other functions. 
 
### Problem 3: Guessing Game with Brute-Force and Random Algorithms 
***Approach***

The program compared two algorithms for guessing three random numbers: 
1. ***Deterministic Brute Force***: 
- Used itertools.permutations to generate all possible patterns of three digits. 
- Iteratively compared each permutation to the target, counting the number of guesses. 
2. ***Pure Random Guessing***: 
- Generated random guesses until the target was matched, or a maximum number of 
attempts was reached. 
3. ***Simulation***: 
- Repeated the guessing process for 10,000 trials and calculated the total, average, 
minimum, and maximum number of guesses.

***Optimizations***
- ***Efficient Permutations***: Used _itertools_ to avoid manually generating permutations, 
reducing complexity. 
- ***Capped Random Guesses***: Limited random guesses to 10,000 tries to handle edge cases 
of infinite loops. 

***Reflection***

This problem provided me insight to the trade-offs between deterministic and probabilistic approaches. With brute force guaranteeing a solution. 
 
### Problem 4: Collatz 3n + 1 Algorithm 
***Approach***

The task involved analyzing the Collatz conjecture for numbers up to 10,000,000 and identifying the top 10 sequences with the longest lengths: 
1. ***Collatz Sequence Generation***: 
- Implemented collatz_sequence_length to calculate the sequence length and largest 
value for a given starting number. 
- Used iterative logic to halve even numbers and apply the 3n + 1 rule for odd numbers. 
2. ***Analysis***: 
- Used over all numbers in the range, storing the sequence length and largest value in a list. 
3. ***Top 10 Sequences***: 
- Sorted the list by sequence length and extracted the top 10 starting numbers. 

***Optimizations***
- Iterative Processing: Avoided recursion to prevent stack overflow and to make efficient 
memory usage. 
- Sorting: Used Python’s efficient Timsort algorithm for sorting sequence data. 

***Reflection***

This problem showcases the challenges used by the Collatz conjecture. It demonstates the 
importance of efficient data handling when analyzing large ranges.