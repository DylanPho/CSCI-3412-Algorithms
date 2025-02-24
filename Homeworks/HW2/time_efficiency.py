'''
Name: Dylan Phoutthavong
Date: 02/16/2025
Course: CSCI 3412
Description: This program reads numbers from a file and sorts them using Insertion Sort and Merge Sort algorithms. It measures the time efficiency of each sorting algorithm and saves the results to a CSV file. It also plots the results using Matplotlib.
'''

import time
import pandas as pd
import matplotlib.pyplot as plt
import os  # To manage file paths

# ---------------- Define Dataset Paths ----------------
DATA_DIR = "/Users/dylanpho/Library/CloudStorage/OneDrive-TheUniversityofColoradoDenver/CU Denver/2024-2025/Spring 2025/CSCI 3412-Algorithms/Homeworks/HW2"

fileNames = ["rand1000.txt", "rand10000.txt", "rand100000.txt", "rand250000.txt", "rand500000.txt", "rand1000000.txt"]
file_paths = {name: os.path.join(DATA_DIR, name) for name in fileNames}  # Absolute paths

# ---------------- Sorting Algorithms ----------------
def insertion_sort(arr):
    """Insertion Sort Algorithm (O(n^2) complexity)"""
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
    """Merge Sort Algorithm (O(n log n) complexity)"""
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
    if not os.path.isfile(filename):  # Check if file exists
        print(f"Error: File '{filename}' does not exist!")
        return []

    with open(filename, 'r') as file:
        return [int(num) for line in file for num in line.split()]

def time_efficiency(func, arr):
    """Measures execution time of a sorting function"""
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

# ---------------- Main Execution ----------------
# Results storage
dataset_sizes = []
insertion_times = []
merge_times = []

# Run sorting tests using the correct file paths
for name, path in file_paths.items():
    numbers = read_numbers_from_file(path)

    if not numbers:  # Skip if the file couldn't be read
        continue

    dataset_sizes.append(len(numbers))

    # Warn if processing a large dataset with Insertion Sort
    if len(numbers) >= 100000:
        print(f"⚠️ WARNING: Running Insertion Sort on {len(numbers)} elements may take a VERY long time!")

    # Measure time for Insertion Sort (now running on all dataset sizes)
    insertion_time = time_efficiency(insertion_sort, numbers)

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

# Display results
print(df_results)

# ---------------- Plot Results ----------------
plt.figure(figsize=(10, 6))
plt.plot(dataset_sizes, merge_times, label="Merge Sort", marker='o', linestyle='-')

# Plot Insertion Sort times where available
plt.plot(dataset_sizes, insertion_times, label="Insertion Sort", marker='s', linestyle='--')

plt.xlabel("Number of Elements")
plt.ylabel("Execution Time (seconds)")
plt.title("Sorting Algorithm Efficiency")
plt.xscale("log")  # Logarithmic scale for better visualization
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.show()