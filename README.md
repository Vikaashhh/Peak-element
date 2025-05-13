# 📈 Day 31 - Find Peak Element

## Problem Statement:
Given an array arr[] where no two adjacent elements are the same, the task is to find the index of a peak element.

A peak element is the one that is greater than its adjacent elements (if they exist).
If multiple peaks are present, return the index of any one of them.

⚠️ Consider the element before the first element and after the last element as -infinity.

## 💡 Approach:
1. Applied a Binary Search-based approach to find the peak element efficiently.

2. At each step, check:

- Is arr[mid] greater than or equal to both neighbors? → Return mid.

- Else if right neighbor is greater → Search right half.

- Else → Search left half.

## Why Binary Search?
Instead of checking every element (O(N)), we used Binary Search (O(log N)) since the property of the array ensures at least one peak exists.

## 🔍 Concepts Used:
- Binary Search (Optimized Search)

- Peak Element Logic

- Handling edge cases using -inf for virtual boundaries

## ⏱ Time & Space Complexity:
- Time Complexity	O(log N)
- Space Complexity	O(1)

## ✅ What I Learned:
1. How to optimize peak element problems using Binary Search instead of linear scanning.

2. Importance of handling array boundaries gracefully (float('-inf')).

3. Correct direction matters in binary search — tiny mistakes can cause TLE.

