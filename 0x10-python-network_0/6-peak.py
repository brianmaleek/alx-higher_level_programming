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
    if not list_of_integers:
        return None

    # lo - lower bound starting index
    # hi - upper bound starting index
    # mid - middle index
    lo, hi = 0, len(list_of_integers) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return list_of_integers[lo]
