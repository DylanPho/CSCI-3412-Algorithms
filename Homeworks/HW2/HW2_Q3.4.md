**Dylan Phoutthavong**

**February 17th, 2025**

**CSCI 3412**

# 3.4 Maintenance

During each iteration of the loop:

- The **smallest remaining element** from `left_half` or `right_half` is compared.
- The smaller element is placed in `arr[k]`, maintaining sorted order.
- The corresponding index (`i` or `j`) is incremented to move to the next element.
- Since **only the next smallest element is added** in each step, the merged portion of `arr` remains correctly sorted.
- The **loop invariant is maintained**, ensuring correctness **throughout execution**.