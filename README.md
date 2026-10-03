# Assignment 4: Heap Data Structures – Implementation, Analysis, and Applications

## Overview

This project explores heap data structures through implementation, theoretical analysis, empirical testing, and a priority-based scheduling application.

The project includes:

1. Heapsort implementation
2. Max-priority queue implementation
3. Priority-based task scheduling simulation
4. Empirical comparison of Heapsort, Quicksort, and Merge Sort
5. Analysis of time complexity, edge cases, and practical applications

## Project Files

- `heapsort.py` - Implements Heapsort using a max-heap and tests multiple edge cases.
- `priority_queue.py` - Implements a max-priority queue with insertion, extraction, peek, and priority-update operations.
- `scheduler_simulation.py` - Demonstrates priority-based task scheduling using the max-priority queue.
- `performance_test.py` - Compares the empirical performance of Heapsort, Quicksort, and Merge Sort.
- `README.md` - Provides project information, execution instructions, and a summary of results.
- `Assignment-4.pdf` - Contains the written analysis, empirical results, discussion, and references.

## Requirements

- Python 3.x
- No external Python libraries are required.

## How to Run the Project

Open a terminal in the project directory.

### Run Heapsort

```bash
python heapsort.py
```

The Heapsort implementation is tested with:

- Random integers
- Already sorted input
- Reverse-sorted input
- Duplicate values
- Negative values
- Mixed positive and negative values
- Single-element input
- Empty input
- All-equal values

All nine test cases completed successfully.

### Run the Max-Priority Queue

```bash
python priority_queue.py
```

The priority queue demonstrates:

- Empty-queue handling
- Task insertion
- `peek_max()` operation
- `extract_max()` operation
- Priority increases
- Rejection of invalid priority decreases
- Extraction in priority order
- Single-task handling
- Duplicate priorities

The priority-order verification produced the expected sequence:

```text
[12, 10, 7, 4, 3]
```

### Run the Scheduler Simulation

```bash
python scheduler_simulation.py
```

The scheduler uses the max-priority queue to process tasks from highest to lowest priority.

For the primary scheduling test, the processed priorities were:

```text
[10, 8, 7, 6, 3, 2, 1]
```

The expected priorities were:

```text
[10, 8, 7, 6, 3, 2, 1]
```

The priority-order verification passed successfully.

The simulation also demonstrates dynamic priority updating. When a routine task becomes urgent, its priority can be increased so that the heap reorganizes and the task is processed according to its new priority.

### Run the Performance Comparison

```bash
python performance_test.py
```

The experiment compares:

- Heapsort
- Quicksort
- Merge Sort

The algorithms are tested using:

- Random input
- Sorted input
- Reverse-sorted input

Input sizes:

- 100
- 500
- 1,000
- 2,000
- 5,000
- 10,000

Each timing measurement is averaged over five trials.

Before collecting timing measurements, correctness and edge-case tests are performed for all three sorting algorithms.

## Empirical Results

At an input size of 10,000, the following execution times were observed:

| Input Distribution | Heapsort (s) | Quicksort (s) | Merge Sort (s) |
|---|---:|---:|---:|
| Random | 0.032304 | 0.014149 | 0.017253 |
| Sorted | 0.028669 | 0.009863 | 0.011698 |
| Reverse Sorted | 0.022135 | 0.009886 | 0.011473 |

The measured results show increasing execution time as input size grows. In this experiment, Quicksort had the lowest measured execution time at an input size of 10,000 for all three tested input distributions.

Empirical execution times may vary depending on the computer, Python environment, and individual execution.

## Heapsort Analysis

Heapsort first constructs a max-heap from the input data and then repeatedly removes the maximum element by exchanging the root with the final element in the active heap.

The major time complexities are:

- Building the max-heap: `O(n)`
- Heapify operation: `O(log n)`
- Overall Heapsort: `O(n log n)`
- Best case: `O(n log n)`
- Average case: `O(n log n)`
- Worst case: `O(n log n)`

This gives Heapsort predictable asymptotic performance regardless of the original ordering of the input.

## Priority Queue Analysis

The max-priority queue is implemented using a binary max-heap.

Major operations include:

| Operation | Time Complexity |
|---|---:|
| `is_empty()` | O(1) |
| `peek_max()` | O(1) |
| `insert()` | O(log n) |
| `extract_max()` | O(log n) |
| Heap adjustment after increasing priority | O(log n) |

As the number of tasks increases, the height of the complete binary heap grows logarithmically. This allows insertion and extraction to remain efficient even as the queue becomes larger.

## Application

The scheduler simulation demonstrates a practical application of a priority queue. Tasks such as critical system alerts, integration messages, data requests, backups, reports, and log reviews can be assigned different priorities.

The max-priority queue allows the scheduler to efficiently select the highest-priority task without sorting the entire task collection after every insertion.

## Conclusion

This project demonstrates the implementation and analysis of heap-based algorithms and data structures. Heapsort provides predictable `O(n log n)` performance, while the max-priority queue efficiently supports priority-based insertion, extraction, and updates.

The empirical experiment also demonstrates how theoretical complexity can be evaluated alongside measured execution times. The scheduling simulation illustrates how a heap-based priority queue can be applied to priority-driven task processing.