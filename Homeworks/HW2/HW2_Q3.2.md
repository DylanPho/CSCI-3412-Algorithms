**Dylan Phoutthavong**

**February 17th, 2025**

**CSCI 3412**

# 3.2 Loop Invariant of the `merge()` Function

The loop invariant in the `merge()` function of Merge Sort in `time_efficiecny.py` is:

> At the start of each iteration of the merging loop, the merged portion of the array contains the smallest elements in sorted order from the left and right subarrays.

This invariant ensures that at **any point in the loop**, the portion of the array that has been merged so far is **correctly sorted**, and the remaining elements in `left_half` and `right_half` are yet to be merged.
