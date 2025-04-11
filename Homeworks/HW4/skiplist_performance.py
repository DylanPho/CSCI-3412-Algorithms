'''
Name: Dylan Phoutthavong
Date: March 8th, 2025
Course: CSCI 3412
Task(s): Implement a complete Skip List class in Python, including insert and search functionalities.

        1. Generate 1 million random integers in the range of 0 to 1,000,000 using a Python program and sort them.

        2. Insert the generated numbers into the skip list.

        3. Create another list of 1 million random different integers (also in the 0–1,000,000 range).

        4. Search each number from Step 4 in the skip list, one at a time, and measure the total time for all 1 million searches.

        5. Repeat the same search process using a binary search on a sorted static list (i.e., the same dataset inserted into the skip list in Step 3, but in a sorted static array).

        - Repeat steps 1 - 5 at least 10 times.
        
        - Display and compare the average time results of the two approaches:

            - Skip List search vs. Binary Search on a sorted list.
'''

import random
import time
import bisect

# SkipList Node definition
class SkipListNode:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

# SkipList class with insert and search
class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipListNode(None, max_level)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if not current or current.value != value:
            rlevel = self.random_level()
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel

            new_node = SkipListNode(value, rlevel)
            for i in range(rlevel + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, value):
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.value == value

# Test and compare performance
def run_experiment(iterations=10, num_elements=1000000, max_val=1000000):
    skip_times, binary_times = [], []

    for run in range(iterations):
        print(f"Run {run + 1}/{iterations}: Generating data...")
        data = sorted(random.sample(range(max_val + 1), num_elements))
        query = random.sample(range(max_val + 1), num_elements)

        # Skip list
        print("Inserting into SkipList...")
        skiplist = SkipList()
        for num in data:
            skiplist.insert(num)

        print("Searching in SkipList...")
        start = time.time()
        for q in query:
            skiplist.search(q)
        skip_time = time.time() - start
        skip_times.append(skip_time)

        # Binary search
        print("Searching in Binary Sorted List...")
        start = time.time()
        for q in query:
            idx = bisect.bisect_left(data, q)
            _ = idx < len(data) and data[idx] == q
        binary_time = time.time() - start
        binary_times.append(binary_time)

        print(f"SkipList Search Time: {skip_time:.4f}s, Binary Search Time: {binary_time:.4f}s\n")

    # Average results
    avg_skip = sum(skip_times) / iterations
    avg_binary = sum(binary_times) / iterations

    print("===== Average Time Results =====")
    print(f"SkipList Search Average Time: {avg_skip:.4f} seconds")
    print(f"Binary Search Average Time:   {avg_binary:.4f} seconds")
    print(f"Speedup:                      {avg_skip / avg_binary:.2f}x (Binary vs SkipList)")

# Run the experiment
run_experiment()