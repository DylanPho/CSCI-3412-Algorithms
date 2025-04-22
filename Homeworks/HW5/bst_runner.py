'''
Name: Dylan Phoutthavong
Date: April 21st, 2025
Course: CSCI 3412
Task(s): 1. Download or copy the BST implementation from the third or fourth link or any other source you like.
        2. Add the following methods to the downloaded code:
            - getHeight () - returns the height of a given tree
            - countNodes() - returns the number of total nodes in a given tree
        3. Create and then fill a BST tree with the integer data from  'rand1000000.txt' file and get the height and number of nodes of the tree using your methods above.
            - Make sure add() and delete() work properly
        4. In-order traversal: Build a new BST from "rand1000.txt" file ( or 100 nodes if you prefer but you may need to make your own data file of 100 nodes)
            - Traverse the tree in descending order and print the keys with a ranking number.  For example, if a key, 418621, is the 534th largest in the tree, display "[534] 418621"
            - You must use the Python "Generator" pattern using 'yield' to display the number in the specified format.
        5. Now, do the same with an RB BST implementation.  You may use the 'pypi'  binary tree package (see the link below) or any other RB tree library you can find on the Internet. Then do steps 2 - 3 (you don't need step 4) with a Red-Black BST tree.
            - https://pypi.org/project/bintrees/  ( a stopped project)
        6. Compare and analyze the height results from both trees (regular BST vs RB BST)
'''

import time
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

    print("\nPerforming inorder traversal...")
    start_traverse = time.time()
    tree.inorder()
    end_traverse = time.time()

    traverse_time = end_traverse - start_traverse
    print(f"\nTraversal completed in {traverse_time:.4f} seconds.")

if __name__ == "__main__":
    main()