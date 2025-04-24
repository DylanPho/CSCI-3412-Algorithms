'''
Name: Dylan Phoutthavong
Date: April 21st, 2025
Course: CSCI 3412
Task(s): 4. In-order traversal: Build a new BST from "rand1000.txt" file ( or 100 nodes if you prefer but you may need to make your own data file of 100 nodes)
            - Traverse the tree in descending order and print the keys with a ranking number.  For example, if a key, 418621, is the 534th largest in the tree, display "[534] 418621"
            - You must use the Python "Generator" pattern using 'yield' to display the number in the specified format.
         5. Now, do the same with an RB BST implementation.  You may use the 'pypi'  binary tree package (see the link below) or any other RB tree library you can find on the Internet. Then do steps 2 - 3 (you don't need step 4) with a Red-Black BST tree.
            - https://pypi.org/project/bintrees/  ( a stopped project)
         6. Compare and analyze the height results from both trees (regular BST vs RB BST)
'''

from BinarySearchTree import Tree

def load_numbers(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            for part in line.strip().split():
                if part.isdigit():
                    numbers.append(int(part))
    return numbers

def main():
    filename = "rand1000.txt"
    output_file = "bst_descending_output.txt"
    numbers = load_numbers(filename)

    tree = Tree()
    for num in numbers:
        tree.insert(num)

    with open(output_file, "w") as f:
        f.write(f"Descending order output from BST ({len(numbers)} values)\n\n")
        for rank, value in enumerate(tree.descending_generator(), start=1):
            f.write(f"[{rank}] {value}\n")

    print(f"Output written to {output_file}")

if __name__ == "__main__":
    main()