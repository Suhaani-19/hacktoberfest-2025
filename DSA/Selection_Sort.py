"""
Selection Sort Algorithm in Python
----------------------------------
Author: Suhaani Garg
Description:
    This script implements the Selection Sort algorithm.
    It repeatedly selects the smallest element from the unsorted
    portion of the array and swaps it with the first unsorted element.

Time Complexity:
    Best Case: O(n²)
    Average Case: O(n²)
    Worst Case: O(n²)
Space Complexity: O(1)
"""

def selection_sort(arr):
    """
    Sorts the given list in ascending order using Selection Sort.
    """
    n = len(arr)
    for i in range(n):
        # Assume the current index has the smallest element
        min_index = i

        # Find the smallest element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    # Example usage
    sample_list = [64, 25, 12, 22, 11]
    print("Original array:", sample_list)
    sorted_list = selection_sort(sample_list)
    print("Sorted array:", sorted_list)
