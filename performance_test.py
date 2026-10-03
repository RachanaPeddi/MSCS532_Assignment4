"""
Assignment 4: Heap Data Structures
Empirical Performance Comparison

This program compares the execution time of:
1. Heapsort
2. Quicksort
3. Merge Sort

The algorithms are tested on random, sorted, and reverse-sorted
input distributions using multiple input sizes and trials.
"""

import random
import time

from heapsort import heapsort


# ---------------------------------------------------------
# Quicksort
# ---------------------------------------------------------

def quicksort(arr):
    """
    Sort a list using Quicksort.

    A middle element is selected as the pivot to avoid consistently
    poor behavior on already sorted and reverse-sorted inputs.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    smaller = [value for value in arr if value < pivot]
    equal = [value for value in arr if value == pivot]
    larger = [value for value in arr if value > pivot]

    return (
        quicksort(smaller)
        + equal
        + quicksort(larger)
    )


# ---------------------------------------------------------
# Merge Sort
# ---------------------------------------------------------

def merge(left, right):
    """
    Merge two sorted lists.
    """
    result = []
    left_index = 0
    right_index = 0

    while (
        left_index < len(left)
        and right_index < len(right)
    ):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def merge_sort(arr):
    """
    Sort a list using Merge Sort.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


# ---------------------------------------------------------
# Input Generation
# ---------------------------------------------------------

def generate_input(size, distribution):
    """
    Generate test data for the requested input distribution.
    """
    if distribution == "Random":
        return [
            random.randint(0, size * 10)
            for _ in range(size)
        ]

    if distribution == "Sorted":
        return list(range(size))

    if distribution == "Reverse Sorted":
        return list(range(size, 0, -1))

    raise ValueError(
        f"Unknown input distribution: {distribution}"
    )


# ---------------------------------------------------------
# Timing
# ---------------------------------------------------------

def time_algorithm(algorithm, data, trials=5):
    """
    Measure the average execution time of a sorting algorithm.

    A fresh copy of the input is used for every trial.
    The output is also verified for correctness.

    Returns:
        float: Average execution time in seconds.
    """
    total_time = 0.0
    expected = sorted(data)

    for _ in range(trials):
        test_data = data.copy()

        start = time.perf_counter()
        result = algorithm(test_data)
        end = time.perf_counter()

        # heapsort modifies its list in place and also returns it.
        if result is None:
            result = test_data

        if result != expected:
            raise AssertionError(
                f"{algorithm.__name__} produced "
                "an incorrect result."
            )

        total_time += end - start

    return total_time / trials


# ---------------------------------------------------------
# Experiment
# ---------------------------------------------------------

def run_experiment():
    """
    Compare Heapsort, Quicksort, and Merge Sort across
    several input sizes and distributions.
    """
    random.seed(532)

    sizes = [
        100,
        500,
        1000,
        2000,
        5000,
        10000,
    ]

    distributions = [
        "Random",
        "Sorted",
        "Reverse Sorted",
    ]

    algorithms = [
        ("Heapsort", heapsort),
        ("Quicksort", quicksort),
        ("Merge Sort", merge_sort),
    ]

    trials = 5

    print("Sorting Algorithm Performance Comparison")
    print("Average execution time over 5 trials")
    print("=" * 88)

    all_results = []

    for distribution in distributions:

        print(f"\nDistribution: {distribution}")
        print("-" * 88)

        print(
            f"{'Size':<10}"
            f"{'Heapsort (s)':<20}"
            f"{'Quicksort (s)':<20}"
            f"{'Merge Sort (s)':<20}"
        )

        print("-" * 88)

        for size in sizes:

            data = generate_input(
                size,
                distribution
            )

            row = {
                "distribution": distribution,
                "size": size,
            }

            times = []

            for name, algorithm in algorithms:

                average_time = time_algorithm(
                    algorithm,
                    data,
                    trials
                )

                row[name] = average_time
                times.append(average_time)

            all_results.append(row)

            print(
                f"{size:<10}"
                f"{times[0]:<20.6f}"
                f"{times[1]:<20.6f}"
                f"{times[2]:<20.6f}"
            )

    return all_results


# ---------------------------------------------------------
# Correctness / Edge-Case Tests
# ---------------------------------------------------------

def run_correctness_tests():
    """
    Verify all three algorithms on important edge cases.
    """
    print("\n\nCorrectness and Edge-Case Verification")
    print("=" * 88)

    test_cases = [
        [],
        [1],
        [5, 5, 5, 5],
        [3, 1, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [-5, 10, 0, -2, 8],
        [4, 2, 4, 1, 2, 4],
    ]

    algorithms = [
        ("Heapsort", heapsort),
        ("Quicksort", quicksort),
        ("Merge Sort", merge_sort),
    ]

    all_passed = True

    for name, algorithm in algorithms:

        algorithm_passed = True

        for test_case in test_cases:

            data = test_case.copy()
            expected = sorted(test_case)

            result = algorithm(data)

            if result is None:
                result = data

            if result != expected:
                algorithm_passed = False
                all_passed = False

        print(
            f"{name:<15} "
            f"edge-case tests passed: "
            f"{algorithm_passed}"
        )

    print("-" * 88)
    print(f"All correctness tests passed: {all_passed}")

    return all_passed


def print_analysis_note():
    """
    Print a short reminder about interpretation of the experiment.
    """
    print("\nExperiment Notes")
    print("=" * 88)

    print(
        "The measured times are empirical results from this "
        "computer and may vary between executions."
    )

    print(
        "The final report should interpret the measured trends "
        "together with the theoretical time and space "
        "complexities of the algorithms."
    )


def main():
    """
    Run the complete empirical comparison.
    """
    run_correctness_tests()

    run_experiment()

    print_analysis_note()

    print("\n" + "=" * 88)
    print("Performance experiment completed successfully.")


if __name__ == "__main__":
    main()