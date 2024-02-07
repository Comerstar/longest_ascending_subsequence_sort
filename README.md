
# Longest Ascending Subsequence Sort

Longest ascending subsequence sort is a sorting algorithm based on finding the longest ascending subsequence.

To run this application, run `python3 longest_ascending_subsequence_sort.py`. The interface expects users to input the list of integers they wish to sort in the order they appear in the list. Alternatively, the defined function `longest_ascending_subsequence_sort(comp, lst)` can be called in code, where `comp` is the comparator for the items of the list (defined as if `x < y`, then `comp(x, y) < 0`, if `x == y`, then `comp(x, y) == 0`, and if `x > y`, then `comp(x, y) > 0`), and `lst` is the list of items to be sorted. The optional parameter `rev` allows users to specify is the remaining items are reversed between iterations. The list will be sorted in ascending order.

## Algorithm

Longest ascending subsequence sort finds the longest ascending subsequence, removes it from the list, and merges it into the sorted list. It repeats it until all of the elements of the list are removed.

## Time Complexity

The maximum time complexity is `n^3`, since it finds the longest ascending substring in `n^2` time, which in the worst case is done `n` times, once for every element of the list.
