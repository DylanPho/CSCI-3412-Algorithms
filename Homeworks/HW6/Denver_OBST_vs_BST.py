'''
Name: Dylan Phoutthavong
Date: May 8th, 2025
Course: CSCI 3412
Task(s): Optimal Binary Search Tree
'''

import random

# Denver word cloud probabilities
denver_prob_dict = {
    'the': 0.0502, 'in': 0.0318, 'to': 0.0301, 'a': 0.0217, 'and': 0.0201,
    'of': 0.0184, 'for': 0.0117, 'day': 0.0117, 'i': 0.0117, 'is': 0.0117,
    'on': 0.0084, 'with': 0.0084, 'family': 0.0067, 'from': 0.0067, 'what': 0.0050,
    've': 0.0050, 'trip': 0.0050, 'my': 0.0050, 'years': 0.0050, 'that': 0.0050,
    'your': 0.0050, 'old': 0.0050, 'his': 0.0050, 'but': 0.0050, 'every': 0.0050,
    'royals': 0.0033, 'out': 0.0033, 'at': 0.0033, 'royal': 0.0033, 'took': 0.0033,
    'up': 0.0033, 'things': 0.0033, 'parents': 0.0033, 'moved': 0.0033, 'us': 0.0033,
    's': 0.0033, 'by': 0.0033, 'people': 0.0033, 'during': 0.0033, 'thanksgiving': 0.0033,
    'it': 0.0033, 'home': 0.0033, 'full': 0.0033, 'casts': 0.0033, 'as': 0.0033,
    'this': 0.0033, 'side': 0.0033, 'guide': 0.0033, 'how': 0.0033, 'nfl': 0.0033
}

# BST Node and insertion
class BSTNode:
    def __init__(self, key, prob):
        self.key = key
        self.prob = prob
        self.left = None
        self.right = None

def insert_bst(root, key, prob):
    if root is None:
        return BSTNode(key, prob)
    if key < root.key:
        root.left = insert_bst(root.left, key, prob)
    else:
        root.right = insert_bst(root.right, key, prob)
    return root

def bst_cost(root, depth=1):
    if root is None:
        return 0
    return depth * root.prob + bst_cost(root.left, depth + 1) + bst_cost(root.right, depth + 1)

# OBST cost calculation
def obst_cost(keys, probs):
    n = len(keys)
    cost = [[0]*n for _ in range(n)]
    for i in range(n):
        cost[i][i] = probs[i]
    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            cost[i][j] = float('inf')
            total_prob = sum(probs[i:j+1])
            for r in range(i, j+1):
                c = (0 if r == i else cost[i][r-1]) + \
                    (0 if r == j else cost[r+1][j]) + total_prob
                if c < cost[i][j]:
                    cost[i][j] = c
    return cost[0][n-1]

# Build and compare
items = list(denver_prob_dict.items())
random.shuffle(items)
keys_shuffled, probs_shuffled = zip(*items)
keys_sorted = sorted(denver_prob_dict.keys())
probs_sorted = [denver_prob_dict[k] for k in keys_sorted]

bst_root = None
for k, p in zip(keys_shuffled, probs_shuffled):
    bst_root = insert_bst(bst_root, k, p)
bst_total = bst_cost(bst_root)
obst_total = obst_cost(keys_sorted, probs_sorted)
improvement = 100 * (1 - obst_total / bst_total)

# Final Output
print("\n--- OBST vs BST Comparison for 'Denver' Query ---")
print(f"BST Cost (random order): {bst_total:.4f}")
print(f"OBST Cost (optimal):     {obst_total:.4f}")
print(f"Improvement:             {improvement:.2f}%")

# Summary
print("\nSummary:")
print(f"For the 'Denver' query, OBST reduced the total search cost by {improvement:.2f}% compared to a randomly built BST.")
