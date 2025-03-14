'''
Name: Dylan Phoutthavong
Date: March 12th, 2025
Course: CSCI 3412
Task(s): a) Implement quicksort and "optimizing" bubble sort. Then, write separate test programs for both algorithms (quicksort and bubble sort) with a test data set of your choice and demonstrate that they work. 
            You may start with the size of 100 unsorted integers for quick testing purposes, then retest it with a larger dataset of at least 1,000 integers.
  
        b) Write code combining both optimizing bubble sort and quicksort algorithms as described in Q1 to find the most optimal k, minimizing the time complexity of your algorithms using 1 M unsorted data used in HW2.   
            In your simulation, you can choose your strategy for determining the granularity of the delta.  You may use the time efficiency program you wrote in the previous homework. 

         c) Write a Python code or use any plotting tool to visualize how time efficiency output correlates to the k value. If you write Python code, you may consider importing "matplotlib.pyplot" library to plot the data.  
            
'''

import time
import random
import matplotlib.pyplot as plt

# Load numbers from file
def load_numbers(filename):
    with open(filename, "r") as file:
        numbers = [int(num) for num in file.read().split()]
    return numbers

# Quicksort algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Optimized Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Hybrid Sort: Uses quicksort until size k, then switches to bubble sort
def hybrid_sort(arr, k):
    if len(arr) <= k:
        return bubble_sort(arr)
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return hybrid_sort(left, k) + middle + hybrid_sort(right, k)

# Measure sorting time
def measure_time(sort_function, arr, k=None):
    start = time.time()
    sorted_arr = sort_function(arr) if k is None else sort_function(arr, k)
    end = time.time()
    return sorted_arr, end - start

# PART (a): TEST CORRECTNESS ON RANDOM ARRAY
print("\n===== PART (A) - TEST SORTING CORRECTNESS =====")

# Generate a random array of 100 integers
random_array = random.sample(range(1, 10000), 100)
print("Original Random Array:")
print(random_array)

# Test sorting on the small array
sorted_qs, _ = measure_time(quicksort, random_array)
sorted_bs, _ = measure_time(bubble_sort, random_array)

print("\nSorted Array using Quicksort:")
print(sorted_qs)

print("\nSorted Array using Bubble Sort:")
print(sorted_bs)

# PART (a) CONTINUED: MEASURE PERFORMANCE ON `rand1000.txt`
print("\n===== PART (A) - EXECUTION TIMES FOR rand1000.txt =====")
rand1000 = load_numbers("rand1000.txt")

_, qs_time = measure_time(quicksort, rand1000)
print(f"Quicksort Execution Time: {qs_time:.5f} seconds")

_, bs_time = measure_time(bubble_sort, rand1000)
print(f"Bubble Sort Execution Time: {bs_time:.5f} seconds")

# PART (b): HYBRID SORT WITH rand1000000.txt
print("\n===== PART (B) - FINDING OPTIMAL k =====")
rand1000000 = load_numbers("rand1000000.txt")

k_values = range(1, 20, 2)  # Test different k values
times = []

for k in k_values:
    _, time_taken = measure_time(hybrid_sort, rand1000000, k)
    times.append(time_taken)
    print(f"k = {k}, Time: {time_taken:.5f} seconds")

# Find optimal k
optimal_k = k_values[times.index(min(times))]
optimal_time = min(times)
print(f"\nOptimal k value: {optimal_k}, Time: {optimal_time:.5f} seconds")

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(k_values, times, marker='o', linestyle='-', label="Sorting Time")
plt.axvline(x=optimal_k, color='r', linestyle='--', label=f"Optimal k = {optimal_k}")
plt.scatter(optimal_k, optimal_time, color='red', zorder=3)
plt.xlabel("k Value")
plt.ylabel("Sorting Time (seconds)")
plt.title("Hybrid Sort Performance vs. k")
plt.legend()
plt.grid(True)
plt.show()
