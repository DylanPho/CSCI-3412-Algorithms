'''
Name: Dylan Phoutthavong
Date: 02/16/2025
Course: CSCI 3412
Description: This program reads numbers from a file and sorts them using Insertion Sort and Merge Sort algorithms. It measures the time efficiency of each sorting algorithm and saves the results to a CSV file. It also plots the results using Matplotlib.
'''

import time
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Sorting Algorithms ----------------
def insertion_sort(arr):
    """Insertion Sort Algorithm (O(n^2) time complexity)"""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Merge Sort Algorithm (O(n log n) time complexity)"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# ---------------- Helper Functions ----------------
def read_numbers_from_file(filename):
    """Reads numbers from a file and returns them as a list of integers"""
    with open(filename, 'r') as file:
        return [int(num) for line in file for num in line.split()]

def time_efficiency(func, arr):
    """Measures execution time of a sorting function"""
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

# ---------------- Main Execution ----------------
fileNames = ["rand1000.txt", "rand10000.txt", "rand100000.txt", "rand250000.txt", "rand500000.txt", "rand1000000.txt"]
file_paths = {name: f"/mnt/data/{name}" for name in fileNames}

# Results storage
dataset_sizes = []
insertion_times = []
merge_times = []

# Run sorting tests using the loop structure from the prompt
for name in fileNames:
    path = file_paths[name]
    numbers = read_numbers_from_file(path)
    dataset_sizes.append(len(numbers))

    # Measure time for Insertion Sort (limited to 100,000 elements)
    if len(numbers) <= 100000:
        insertion_time = time_efficiency(insertion_sort, numbers)
    else:
        insertion_time = None  # Too slow for larger datasets

    # Measure time for Merge Sort
    merge_time = time_efficiency(merge_sort, numbers)

    insertion_times.append(insertion_time)
    merge_times.append(merge_time)

# Prepare DataFrame with results
df_results = pd.DataFrame({
    "Dataset Size": dataset_sizes,
    "Insertion Sort Time (s)": insertion_times,
    "Merge Sort Time (s)": merge_times,
})

# Display results in a table
print(df_results)

# ---------------- Plot Results ----------------
plt.figure(figsize=(10, 6))
plt.plot(dataset_sizes, merge_times, label="Merge Sort", marker='o', linestyle='-')

# Only plot Insertion Sort times where available
insertion_sizes = [size for size, time in zip(dataset_sizes, insertion_times) if time is not None]
insertion_times_filtered = [time for time in insertion_times if time is not None]

plt.plot(insertion_sizes, insertion_times_filtered, label="Insertion Sort", marker='s', linestyle='--')

plt.xlabel("Number of Elements")
plt.ylabel("Execution Time (seconds)")
plt.title("Sorting Algorithm Efficiency")
plt.xscale("log")  # Logarithmic scale for better visualization
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.show()