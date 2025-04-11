**Dylan Phoutthavong**

**March 7th, 2025**

**CSCI 3412**

# HW4 Outputs & Answers

### Q1) Merging k sorted lists into one sorted list (25 points)

#### - (5 points) Describe your algorithm in high-level pseudocode and explain why your algorithm meets O(n log k) time efficiency in English. 

Input: k sorted lists, each containing elements in ascending order
Output: One fully sorted list containing all elements

1. Create an empty min-heap (priority queue)
2. For each sorted list:
     a. Push the first element into the min-heap along with:
         - Its value
         - The list index
         - The index of the element within the list
3. While the min-heap is not empty:
     a. Pop the smallest element from the heap
     b. Add its value to the final merged list
     c. If there is a next element in the same list:
         i. Push the next element into the heap with updated indices
4. Return the merged list

### Why This Algorithm Is O(n log k):
- At any point, the heap contains at most k elements (one from each list).

- Inserting and removing from the heap takes O(log k) time.

- We perform these operations n times total, once per element.

- So the total time complexity is O(n log k).

This is more efficient than a naive approach like repeated pairwise merging or appending all elements and sorting them (which can take O(nk) or O(n log n), depending on the method)

<mark>Program Output:<mark>
```

```

<mark>Program Output:<mark>

```
Reading and splitting the data...
Sorting 50 sublists with Radix Sort...
Sorting the remaining 50 sublists with Bucket Sort...
Merging with O(n log k) heap-based merge...
O(n log k) Merge completed in 0.2935 seconds.
Merging with O(nk) naive merge...
O(nk) Merge completed in 0.0643 seconds.

--- Performance Summary ---
O(n log k) Merge Time: 0.2935 seconds
O(nk) Merge Time:     0.0643 seconds
Speedup:              0.22x faster using heap-based merge

Sample Output (First 10 values from each merged list):
Heap Merge: [0, 1, 2, 3, 3, 3, 5, 5, 5, 6]
Naive Merge: [0, 1, 2, 3, 3, 3, 5, 5, 5, 6]
```

### Q2) Skiplist Performance Experiment (5 points)

<mark>Program Output:<mark>

```
Run 1/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 3.2749s, Binary Search Time: 0.4488s

Run 2/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 3.1477s, Binary Search Time: 0.4771s

Run 3/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 3.0707s, Binary Search Time: 0.4520s

Run 4/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 2.9063s, Binary Search Time: 0.4523s

Run 5/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 2.8707s, Binary Search Time: 0.4535s

Run 6/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 2.9444s, Binary Search Time: 0.4493s

Run 7/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 2.9786s, Binary Search Time: 0.4603s

Run 8/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 2.8739s, Binary Search Time: 0.4536s

Run 9/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 3.0945s, Binary Search Time: 0.4468s

Run 10/10: Generating data...
Inserting into SkipList...
Searching in SkipList...
Searching in Binary Sorted List...
SkipList Search Time: 3.1300s, Binary Search Time: 0.4559s

===== Average Time Results =====
SkipList Search Average Time: 3.0292 seconds
Binary Search Average Time:   0.4549 seconds
Speedup:                      6.66x (Binary vs SkipList)
```

### Do the results match my expectations?
Yes, the results matched my expectations. Although both search methods are O(log n) in theory, I expected the binary search to perform better in practice due to the following reasons:

- Memory layout: Python lists are stored in contiguous memory, which takes better advantage of CPU cache.

- Lower overhead: Binary search doesn’t involve random level jumps or pointer chasing.

- Highly optimized C backend: Python’s bisect module is implemented in C and runs much faster than a custom class like Skip List written in Python.

The Skip List search times were consistent and reasonable but understandably slower, reinforcing the idea that theoretical performance doesn’t always translate directly to real-world speed.

### AI Reflection
I used an AI tool ChatGPT that was extremely helpful throughout this portion of the assignment:

- Saved time building the Skip List class with insert and search logic.

- Helped generate efficient benchmarking code and interpret the results.

- Let me focus more on analyzing data structure behavior rather than debugging syntax or boilerplate.

This experiment gave me practical insight into why we need to consider data locality, language-level optimizations, and implementation overhead—not just Big-O notation—when designing for performance.

### Q3) Answer the following BST questions, a) - e) (Total 10 points)

#### a). (2 points) Assign the keys 62, 141, 15, 37, 71, 121, 75, 171, 101, and 93 to the nodes of the binary search tree shown below. Feel free to do trial and error to fill the tree with the given list of keys, and you are allowed to rearrange the keys as long as the tree maintains the BST properties. Show the BST tree filled with the keys in the list. 

Given Keys:
`62, 141, 15, 37, 71, 121, 75, 171, 101, and 93`

**Step**: Rearrange the values to fit the given tree shape while maintaining BST properties:

1. Sort the keys:
`15, 37, 62, 71, 75, 93, 101, 121, 141, 171`

2. Perform an **in-order traversal** of the BST shape and assign sorted values in order to preserve BST rules.

**Resulting BST with keys filled (In-order assignment)**:
![plot image](./execution_Q3_plot.png)

#### b). (2 points) A list of random keys and a tree is given to you.  The tree's shape is fixed. i.e., you can't change its shape but you are allowed to rearrange the keys. The number of keys in the given list is the same as the number of available nodes of the tree. 

#### Now, we want to find a way to systematically insert the keys in the list into the tree while keeping it a BST. This solution will solve question a) above systematically.  Describe an algorithm to fill the tree.

**Goal**: Insert the keys into the given fixed tree shape so it remains a valid BST.

**Algorithm**:

1. Sort the list of keys in ascending order.
2. Traverse the given tree structure in **in-order** (left, root, right).
3. Assign each visited node the next smallest key from the sorted list.

This ensures BST properties are preserved: all left descendants are smaller, and all right descendants are greater.

#### c). (2 points) Starting from the root node, we want to populate a BST with the keys in any given list without altering the key order. i.e. you can't rearrange the keys.  Using the keys and the tree in question a) as an example,

   #### i) Display the ordered list of the keys that can be sequentially inserted into the tree. 

    [15, 37, 62, 71, 75, 93, 101, 121, 141, 171]

   #### ii) Describe an algorithm to get the list above systematically.

   **Algorithm** (starting from the root):

1. Use a queue or recursive helper to traverse the tree in in-order.

2. Maintain an external index or iterator to track the current key.

3. At each node, assign the current key and increment the index.

4. Recursively apply this to left and right subtrees.

This ensures all keys are inserted into the tree in their original order without violating the BST property.

#### d). (2 points) Describe why this specific instance of the binary search tree below can't be colored to form a valid red-black tree even without populating keys.

A valid Red-Black Tree (RBT) must satisfy:

1. Every node is red or black.

2. Root is always black.

3. Red nodes cannot have red children (no two reds in a row).

4. Every path from root to leaves has the same number of black nodes.

**Why this shape fails**:

- The left-heavy chain of nodes at the bottom (e.g., nodes with values like 71 → 75 → 93) creates a path with too many nodes in one direction.

- It becomes impossible to balance the black height across all paths.

- Attempts to color red and black will violate either the red-red rule or result in uneven black heights.

Thus, the tree's structure violates RBT properties regardless of key values.

#### e). (2 points) Now let's try to do two rotations to make it an RB tree.  Describe how rotations are performed and show the final picture of an RB binary search tree where each key is properly decorated with a key and a color.

To fix imbalance and make it a valid Red-Black Tree:

1. **Left Rotation** on node 71:

   - Promotes 75 above 71 and pushes 71 to the left.

2. **Right Rotation** on node 101:

   - Balances the tree by promoting 75 as the new root of the subtree.

**Resulting RB Tree**:
![plot image](./execution_Q3_plot.png)

Each node can be assigned a color such that:

- No red node has a red child.

- All paths from root to leaf contain the same number of black nodes.

