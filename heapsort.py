"""
Assignment 4: Heap Data Structures
Heapsort Implementation

This module implements Heapsort using a max-heap.
The implementation sorts the input list in ascending order.
"""


def max_heapify(arr, heap_size, root_index):
    """
    Restore the max-heap property for the subtree rooted at root_index.

    Parameters:
        arr (list): List containing the heap.
        heap_size (int): Number of elements currently in the heap.
        root_index (int): Index of the subtree root.
    """
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    # Check whether the left child is larger than the root.
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # Check whether the right child is larger than the current largest.
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # If the largest value is not the root, swap and continue heapifying.
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        max_heapify(arr, heap_size, largest)


def build_max_heap(arr):
    """
    Convert a list into a max-heap in place.

    Parameters:
        arr (list): List to convert into a max-heap.
    """
    n = len(arr)

    # All elements after the last non-leaf node are already valid heaps.
    for index in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, index)


def heapsort(arr):
    """
    Sort a list in ascending order using Heapsort.

    Parameters:
        arr (list): List to sort.

    Returns:
        list: The sorted list.
    """
    n = len(arr)

    # Empty and single-element lists are already sorted.
    if n <= 1:
        return arr

    # Step 1: Build a max-heap.
    build_max_heap(arr)

    # Step 2: Repeatedly move the maximum element to the end.
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]

        # Restore the max-heap property for the remaining heap.
        max_heapify(arr, end, 0)

    return arr


def run_test(test_name, input_data):
    """
    Run one Heapsort test and verify the result.

    Parameters:
        test_name (str): Description of the test.
        input_data (list): Values to sort.
    """
    original = input_data.copy()
    expected = sorted(input_data)
    result = heapsort(input_data.copy())

    print(f"\n{test_name}")
    print(f"Original: {original}")
    print(f"Sorted:   {result}")
    print(f"Expected: {expected}")
    print(f"Passed:   {result == expected}")


def main():
    """
    Test Heapsort using normal inputs and important edge cases.
    """
    print("Heapsort Implementation Tests")
    print("=" * 50)

    test_cases = [
        (
            "Test 1 - Random integers",
            [12, 11, 13, 5, 6, 7]
        ),
        (
            "Test 2 - Already sorted",
            [1, 2, 3, 4, 5, 6]
        ),
        (
            "Test 3 - Reverse sorted",
            [6, 5, 4, 3, 2, 1]
        ),
        (
            "Test 4 - Duplicate values",
            [4, 2, 4, 1, 2, 4, 3]
        ),
        (
            "Test 5 - Negative values",
            [-5, -1, -10, 3, 0, 2]
        ),
        (
            "Test 6 - Mixed positive and negative values",
            [10, -3, 7, 0, -8, 4, 4]
        ),
        (
            "Test 7 - Single element",
            [42]
        ),
        (
            "Test 8 - Empty list",
            []
        ),
        (
            "Test 9 - All equal values",
            [5, 5, 5, 5, 5]
        )
    ]

    for test_name, test_data in test_cases:
        run_test(test_name, test_data)

    print("\n" + "=" * 50)
    print("All Heapsort tests completed.")


if __name__ == "__main__":
    main()