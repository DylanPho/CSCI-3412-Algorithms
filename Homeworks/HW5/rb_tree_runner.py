'''
Name: Dylan Phoutthavong
Date: April 22nd, 2025
Course: CSCI 3412
Task(s): 5. Now, do the same with an RB BST implementation.  You may use the 'pypi'  binary tree package (see the link below) or any other RB tree library you can find on the Internet. Then do steps 2 - 3 (you don't need step 4) with a Red-Black BST tree.
            - https://pypi.org/project/bintrees/  ( a stopped project)
         6. Compare and analyze the height results from both trees (regular BST vs RB BST)
'''

from sortedcontainers import SortedSet
import time
import math

class RedBlackTreeSimulator:
    def __init__(self):
        self.tree = SortedSet()

    def insert(self, value):
        self.tree.add(value)

    def count_nodes(self):
        return len(self.tree)

    def get_height(self):
        return int(math.log2(len(self.tree))) + 1 if self.tree else 0

    def descending_generator(self):
        for val in reversed(self.tree):
            yield val

def load_numbers(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            for part in line.strip().split():
                if part.isdigit():
                    numbers.append(int(part))
    return numbers

def main():
    filename = "rand1000000.txt"
    output_file = "rb_tree_output.txt"
    numbers = load_numbers(filename)

    tree = RedBlackTreeSimulator()

    start = time.time()
    for num in numbers:
        tree.insert(num)
    end = time.time()

    insert_time = end - start
    node_count = tree.count_nodes()
    tree_height = tree.get_height()

    with open(output_file, "w") as out:
        out.write("Red-Black Tree Simulation Summary\n")
        out.write("----------------------------------\n")
        out.write(f"Inserted Nodes: {node_count}\n")
        out.write(f"Insertion Time: {insert_time:.4f} seconds\n")
        out.write(f"Estimated Height (log2N): {tree_height}\n\n")
        out.write("Top 10 Values in Descending Order:\n\n")
        for rank, value in enumerate(tree.descending_generator(), start=1):
            if rank > 10:
                break
            out.write(f"[{rank}] {value}\n")

    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()