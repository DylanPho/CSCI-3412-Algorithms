**Dylan Phoutthavong**

**February 17th, 2025**

**CSCI 3412**


# Q2 Time efficiency between good and not-so-good sorting algorithms 

## Overview

This assignment evaluates the time efficiency of **Insertion Sort** and **Merge Sort** across various dataset sizes ranging from **1,000 to 1,000,000 elements**. The results were obtained by measuring execution time for both sorting algorithms.

### Total Execution Time: ~9-10 hours

## Execution Results

| Dataset Size | Intertion Sort Time (s) | Merge Sort Time (s) |
|:---:         |:---:                    |:---:                |
|    1,000     |        0.010569         |       0.000860      |
|    10,000    |        1.212569         |       0.012101      |
|    100,000   |        118.4697519      |       0.151744      |
|    250,000   |        755.202096       |       0.418384      |
|    500,000   |  3,300.05348 (~55 min)  |       0.890694      |
|    1,000,000 | 20,784.469284 (~5.8 hrs)|       1.941502      |

## Analysis of Results

### Insertion Sort Performance

- **Scalability Issue**: Insertion Sort's execution time grows quadratically as dataset size increases (**O($n^2$)** complexity).

- **Severe Performance Drop**: At **1,000,000 elements**, Insertion Sort took over **5 hours** to complete.

- **Impractical for Large Datasets**: The time required for Insertion Sort makes it impractical for datasets larger than **100,000 elements**.

### Merge Sort Performance
- **Scalability Strength**: Merge Sort's execution time grows logarithmically (**O(n log n) complexity**).

- **Handles Large Datasets Efficiently**: At **1,000,000 elements**, Merge Sort finished in **~2 seconds**, significantly outperforming Insertion Sort.

- **Best Choice for Large Inputs**: Merge Sort remains practical and efficient across all tested dataset sizes.

## Key Observations
1. Insertion Sort is only suitable for **small datasets (≤10,000 elements)**.

   - Beyond **100,000 elements**, it becomes too slow for practical use.

2. Merge Sort outperforms Insertion Sort on all dataset sizes.
   - Even at **1,000,000 elements**, Merge Sort completes in under **2 seconds**, while Insertion Sort takes 5+ hours.

3. **Big-O Complexity Confirmation**:
   - This assignment confirms the theoretical complexity of both sorting algorithms:

     - Insertion Sort: 𝑂($𝑛^2$) → Execution time **increases quadratically**.
     - Merge Sort: 𝑂(𝑛 log⁡ 𝑛) → Execution time **scales efficiently**.

## Conclusions & Recommendations

- **Avoid Insertion Sort** for datasets larger than **10,000 elements**.

- Always use **Merge Sort** for **medium to large** datasets due to its superior efficiency.

- **Future Optimizations**: Consider using **Quicksort or Timsort** for even better performance.

## Lessons Leanred
- Running inefficient algorithms on large datasets can **lead to excessive computation time**.

- **Choosing the right algorithm for the dataset size is critical** for efficiency.

- Merge Sort demonstrates how **divide-and-conquer** algorithms outperform simpler methods for large-scale sorting.
