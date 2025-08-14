# Remove Duplicates from Sorted Array

  **Link:** [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array)  
  **Difficulty:** Easy  
  **Tags:** Array, Two Pointers 

## Solutions
- [Python](remove-duplicates-from-sorted-array.py)
- [C++](remove-duplicates-from-sorted-array.cpp)

## Approach
In my oppinion this is the perfect case scenario to use two pointers, and that's what I've done.
I iterated through the array with two pointers, one responsible for each unique number and the second one checking whether the following numbers are different from the number that is represented by the first pointer at the current position. In case it was different I incremented first pointer's value and then replaced it with the value that is represented by the second pointer, otherwise I went to the next element with the second pointer.
There was no need to do anything else since in the description it says that the assertion is made until k, so we don't care what comes in the array after the number of unique elements (the number we returned).