**Dylan Phoutthavong**

**February 17th, 2025**

**CSCI 3412**

# 3.1 General Description of Loop Invariant Technique

A **loop invariant** is a property that holds **before and after** each iteration of a loop. It is used as a proof technique to show that an algorithm maintains correctness at every step. A loop invariant proof consists of three key steps:

1. **Initialization**: The invariant is true before the loop starts.

2. **Maintenance**: If the invariant is true before an iteration, it remains true after the iteration.

3. **Termination**: When the loop terminates, the invariant provides insight into the correctness of the algorithm.
By proving that an invariant holds throughout the loop execution, we can confirm that an algorithm is correct.

Using a **loop invariant proof** ensures that the `merge()` function in Merge Sort **produces a correctly sorted array**.