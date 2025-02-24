**Dylan Phoutthavong**

**February 17th, 2025**

**CSCI 3412**

# 3.3 Initialization

Before the loop starts:

- The two subarrays `left_half` and `right_half` are already sorted due to **recursive calls**.
- Three indices **(i, j, k)** are initialized:
    - `i = 0` → Tracks the position in `left_half`
    - `j = 0` → Tracks the position in `right_half`
    - `k = 0` → Tracks the position in `arr` (the merged array)
- The **loop invariant holds initially** because the merged array is empty, which is slightly sorted.