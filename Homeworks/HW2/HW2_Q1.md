**Dylan Phoutthavong**

**February 16th, 2025**

**CSCI 3412**

# Q1  Problem solving: Comparison of Running Times - Explanation

## Introduction

This markdown explains how the values in the "Comparison of Running Times" table were calculated. The goal is to determine the maximum problem size $n$ that can be solved in a given time $t$, assuming the algorithm takes $f(n)$ microseconds to execute.

The available time units:

- **1 second** = $10^6$ microseconds

- **1 minute** = $10^6$ microseconds

- **1 hour** = $10^6$ microseconds

- **1 day** = $10^6$ microseconds

- **1 month** = $10^9$ microseconds

- **1 year** = $10^13$ microseconds

- **1 century** = $10^15$ microseconds

## Calculations for Each Function

### 1.  Logarithmic Complexity: $logn$
- Formula: $log n = t$ --> $n = 2^t$

- Example: For 1 second, $n=2^(10^6)$ , which is an extremely large number.

### 2. Square Root Complexity: $\sqrt{n}$
- Formula: $\sqrt{n} = t$ -> $n = t^2$

- Example: For 1 second, $n=(10^6)^2=10^(12)$.

### 3. Linear Complexity: $n$
- Formula: $n=t$

- Example: For 1 second, $n=10^6$.

### 4. Linearithmic Complexity: $𝑛log𝑛$
- Approximation: $n$ $\approx$ $\frac{t}{logn}$, solved iteratively.

- Example: For 1 second, $n$ $\approx$ $5 * 10^4$.

### 5. Quadratic Complexity: $n^2$
- Formula: $n^2=t$ --> $n=\sqrt{t}$

- Example: For 1 second, $n=\sqrt{10^6}=10^3$.

### 6. Cubic Complexity: $n^3$
- Formula: $n^3=t$ --> $n=\sqrt[3]{t}$

- Example: For 1 second, $n=\sqrt{10^6}=10^3$.

### 7. Exponential Complexity: $2^n$
- Formula: $2^n=t$ --> $n=log_2t$

- Example: For 1 second, $n=log_2(10^6)\approx19$.

### 8.  Factorial Complexity: $n!$
- Approximation: $n!(n/e)^n$, solved iteratively.

- Example: For 1 second, $n\approx11$

## Conclusion

These calculations demonstrate how **computational complexity affects problem size limits**. While **logarithmic and linear algorithms** can handle massive inputs, **exponential and factorial complexities** quickly become impractical.

This highlights the importance of selecting efficient algorithms for large-scale computations.