'''
Name: Dylan Phoutthavong
Date: March 7th, 2025
Course: CSCI 3412
Task(s): Write a Python code to implement your algorithm described above with the following data:
            1. Read the integers from rand1000000.txt of HW2. Split it into 100 rand10000 lists.  Feel free to use your file naming convention of those sub-lists for easier save and read operations
            2. Sort 50 sublists  with Radix sorts with counting sort as underlying sort for each digit
            3. The remaining 50  sublists with bucket sorts.
            4. Finally, merge the 100 sorted sublists into one sorted list using the merging algorithm you specified above.
'''

import time
import heapq

# Step 1: Read and split file into 100 lists of size 10,000
def read_and_split_file(filename, num_sublists=100):
    with open(filename, 'r') as f:
        numbers = [int(num) for line in f for num in line.strip().split()]
    
    sublist_size = len(numbers) // num_sublists
    return [numbers[i * sublist_size: (i + 1) * sublist_size] for i in range(num_sublists)]

# Step 2a: Radix Sort with Counting Sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# Step 2b: Bucket Sort
def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    bucket_count = 10
    max_val, min_val = max(arr), min(arr)
    bucket_range = (max_val - min_val + 1) / bucket_count
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Step 3: Merge k sorted lists using min-heap
def merge_sorted_lists_heap(sorted_lists):
    heap = []
    result = []
    
    for i, lst in enumerate(sorted_lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, val_idx = heapq.heappop(heap)
        result.append(val)
        if val_idx + 1 < len(sorted_lists[list_idx]):
            next_tuple = (sorted_lists[list_idx][val_idx + 1], list_idx, val_idx + 1)
            heapq.heappush(heap, next_tuple)
    
    return result

# Step 4: Naive merge O(nk) for performance comparison
def merge_sorted_lists_naive(sorted_lists):
    merged = []
    for lst in sorted_lists:
        merged += lst
    return sorted(merged)

# Main function
def process_and_merge(filename):
    print("Reading and splitting the data...")
    sublists = read_and_split_file(filename)
    
    print("Sorting 50 sublists with Radix Sort...")
    for i in range(50):
        sublists[i] = radix_sort(sublists[i])
    
    print("Sorting the remaining 50 sublists with Bucket Sort...")
    for i in range(50, 100):
        sublists[i] = bucket_sort(sublists[i])
    
    print("Merging with O(n log k) heap-based merge...")
    start_time = time.time()
    merged_heap = merge_sorted_lists_heap(sublists)
    heap_time = time.time() - start_time
    print(f"O(n log k) Merge completed in {heap_time:.4f} seconds.")
    
    print("Merging with O(nk) naive merge...")
    start_time = time.time()
    merged_naive = merge_sorted_lists_naive(sublists)
    naive_time = time.time() - start_time
    print(f"O(nk) Merge completed in {naive_time:.4f} seconds.")
    
    print("\n--- Performance Summary ---")
    print(f"O(n log k) Merge Time: {heap_time:.4f} seconds")
    print(f"O(nk) Merge Time:     {naive_time:.4f} seconds")
    print(f"Speedup:              {naive_time / heap_time:.2f}x faster using heap-based merge\n")
    
    print("Sample Output (First 10 values from each merged list):")
    print("Heap Merge:", merged_heap[:10])
    print("Naive Merge:", merged_naive[:10])
    
    return merged_heap, merged_naive

# Execute the processing
filename = "rand1000000.txt"
merged_heap_result, merged_naive_result = process_and_merge(filename)
