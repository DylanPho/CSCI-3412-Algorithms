'''
Name: Dylan Phoutthavong
Date: March 10th, 2025
Course: CSCI 3412
Task(s): Below is a max_heapify() function implemented using the recursive function method. Convert it to an iterative version instead of recurrence. 
            Then, test both functions using 1M random integer data from HW2 with the timeEfficiency() function implemented in HW1b. Finally,  compare the execution times and determine which function runs faster.  
            You may also implement build_heap() and build_max_heap() functions.  See slide 12 for the build_max_heap() code.

'''

import time
import os

# ---------------- Helper Function ----------------
def read_numbers_from_file(filename):
    """Reads numbers from a file and returns them as a list of integers"""
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist!")
        return []

    with open(filename, 'r') as file:
        return [int(num) for line in file for num in line.split()]

# ---------------- Heap Functions ----------------
# Recursive max_heapify function
def max_heapify_recursive(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array)
    largest = i

    if left < length and array[left] > array[largest]:
        largest = left
    if right < length and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify_recursive(array, largest)

# Iterative max_heapify function
def max_heapify_iterative(array, i):
    length = len(array)

    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < length and array[left] > array[largest]:
            largest = left
        if right < length and array[right] > array[largest]:
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            i = largest  # Continue heapifying the affected subtree
        else:
            break

# Build max heap using recursive max_heapify
def build_max_heap_recursive(array):
    for i in reversed(range(len(array) // 2)):
        max_heapify_recursive(array, i)

# Build max heap using iterative max_heapify
def build_max_heap_iterative(array):
    for i in reversed(range(len(array) // 2)):
        max_heapify_iterative(array, i)

# Function to measure execution time
def timeEfficiency(func, *args, **kwargs):
    start_time = time.perf_counter()  # Start time
    func(*args, **kwargs)  # Execute function
    end_time = time.perf_counter()  # End time

    total_time = end_time - start_time  # Calculate execution time
    return total_time  # Return execution time for comparison

# ---------------- Testing Function ----------------
def test_heap_efficiency(filename):
    numbers = read_numbers_from_file(filename)

    if not numbers:
        print("No data to process. Exiting...")
        return

    print(f"Processing {len(numbers)} numbers from {filename}...\n")

    # Measure Recursive Max-Heapify
    test_data1 = numbers.copy()
    recursive_time = timeEfficiency(build_max_heap_recursive, test_data1)
    print(f"Recursive max_heapify Execution Time: {recursive_time:.5f} seconds")

    # Measure Iterative Max-Heapify
    test_data2 = numbers.copy()
    iterative_time = timeEfficiency(build_max_heap_iterative, test_data2)
    print(f"Iterative max_heapify Execution Time: {iterative_time:.5f} seconds")

    # Determine which function is faster
    if iterative_time < recursive_time:
        percent_faster = ((recursive_time - iterative_time) / recursive_time) * 100
        print(f"\n✅ Iterative max_heapify is {percent_faster:.2f}% faster than Recursive max_heapify.")
    else:
        percent_faster = ((iterative_time - recursive_time) / iterative_time) * 100
        print(f"\n✅ Recursive max_heapify is {percent_faster:.2f}% faster than Iterative max_heapify.")

# ---------------- Run the Test ----------------
filename = "/Users/dylanpho/Library/CloudStorage/OneDrive-TheUniversityofColoradoDenver/CU Denver/2024-2025/Spring 2025/CSCI 3412-Algorithms/Homeworks/HW3/rand1000000.txt"  # Path to uploaded file
test_heap_efficiency(filename)