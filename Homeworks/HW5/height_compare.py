'''
Name: Dylan Phoutthavong
Date: April 22nd, 2025
Course: CSCI 3412
Task(s): 6. Compare and analyze the height results from both trees (regular BST vs RB BST)
'''

def print_height_comparison(bst_height, rb_height):
    print("\nHeight Comparison Chart:")
    print("------------------------")
    print(f"BST Height:     {bst_height}  " + "#" * (bst_height // 100))
    print(f"RB Tree Height: {rb_height}  " + "#" * (rb_height // 2))

# Example values from earlier output
if __name__ == "__main__":
    bst_height = 9742
    rb_height = 20
    print_height_comparison(bst_height, rb_height)