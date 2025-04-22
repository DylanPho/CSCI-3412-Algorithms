'''
Name: Dylan Phoutthavong
Date: April 21st, 2025
Course: CSCI 3412
Task(s): 2. Add the following methods to the downloaded code:
            - getHeight () - returns the height of a given tree
            - countNodes() - returns the number of total nodes in a given tree
         3. Create and then fill a BST tree with the integer data from  'rand1000000.txt' file and get the height and number of nodes of the tree using your methods above.
            - Make sure add() and delete() work properly
'''

import time
import math
from BinarySearchTree import Tree

def load_numbers(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            # Split line by whitespace and filter out empty strings
            parts = line.strip().split()
            for part in parts:
                if part.isdigit():
                    numbers.append(int(part))
    return numbers

def main():
    filename = input("Enter filename (e.g., rand1000.txt or rand1000000.txt): ").strip()
    numbers = load_numbers(filename)

    print(f"\nInserting {len(numbers)} values into BST...")
    tree = Tree()

    start_insert = time.time()
    for num in numbers:
        tree.insert(num)
    end_insert = time.time()

    insert_time = end_insert - start_insert
    print(f"Insertion completed in {insert_time:.4f} seconds.")

    # Get height and count
    total_nodes = tree.count_nodes()
    height = tree.get_height()
    optimal_height = int(math.log2(total_nodes)) + 1

    print(f"\nTree Height: {height}")
    print(f"Total Nodes: {total_nodes}")
    print(f"Optimal Height (balanced tree): {optimal_height}")

    # Heuristic balance check
    if height <= 2 * optimal_height:
        print("Balance Status: Likely Balanced")
    else:
        print("Balance Status: Likely Unbalanced / Skewed")

if __name__ == "__main__":
    main()