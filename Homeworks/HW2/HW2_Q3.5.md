**Dylan Phoutthavong**

**February 17th, 2025**

**CSCI 3412**

# 3.5 Termination

When the loop terminates:

- Either `left_half` or `right_half` is fully merged into `arr`.
- Any **remaining elements** (from the non-empty half) are already sorted and are **appended directly**.
- At this point, the **entire array is fully merged and sorted**.
- Since the **loop invariant was maintained in every iteration**, the final array is correctly sorted.