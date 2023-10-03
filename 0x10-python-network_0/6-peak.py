#!/usr/bin/python3
"""
function finds a peak in a list of unsorted integers.
1. Prototype: def find_peak(list_of_integers):
2. You are not allowed to import any module
3. Your algorithm must have the lowest complexity
4. 6-peak.txt must contain the complexity of your
    algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
"""


def find_peak(list_of_integers):
    # Edge case: if the list is empty, there is no peak.
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
