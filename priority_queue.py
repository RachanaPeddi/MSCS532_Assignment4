"""
Assignment 4: Heap Data Structures
Priority Queue Implementation

This module implements a max-priority queue using a binary heap.
Tasks with larger priority values are processed before tasks with
smaller priority values.
"""


class Task:
    """
    Represents a task stored in the priority queue.

    Attributes:
        task_id (int): Unique identifier for the task.
        description (str): Description of the task.
        priority (int): Priority value of the task.
    """

    def __init__(self, task_id, description, priority):
        self.task_id = task_id
        self.description = description
        self.priority = priority

    def __repr__(self):
        return (
            f"Task(id={self.task_id}, "
            f"description='{self.description}', "
            f"priority={self.priority})"
        )


class MaxPriorityQueue:
    """
    Implements a max-priority queue using a binary heap.
    """

    def __init__(self):
        self.heap = []

    def _parent(self, index):
        """Return the parent index."""
        return (index - 1) // 2

    def _left(self, index):
        """Return the left-child index."""
        return 2 * index + 1

    def _right(self, index):
        """Return the right-child index."""
        return 2 * index + 2

    def _swap(self, first, second):
        """Swap two elements in the heap."""
        self.heap[first], self.heap[second] = (
            self.heap[second],
            self.heap[first],
        )

    def _heapify_up(self, index):
        """
        Restore the max-heap property by moving an element upward.
        """
        while index > 0:
            parent = self._parent(index)

            if self.heap[parent].priority >= self.heap[index].priority:
                break

            self._swap(parent, index)
            index = parent

    def _heapify_down(self, index):
        """
        Restore the max-heap property by moving an element downward.
        """
        size = len(self.heap)

        while True:
            largest = index
            left = self._left(index)
            right = self._right(index)

            if (
                left < size
                and self.heap[left].priority
                > self.heap[largest].priority
            ):
                largest = left

            if (
                right < size
                and self.heap[right].priority
                > self.heap[largest].priority
            ):
                largest = right

            if largest == index:
                break

            self._swap(index, largest)
            index = largest

    def is_empty(self):
        """
        Return True when the priority queue contains no tasks.
        """
        return len(self.heap) == 0

    def insert(self, task):
        """
        Insert a new task into the priority queue.

        Time complexity:
            O(log n)
        """
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be inserted.")

        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def peek_max(self):
        """
        Return the highest-priority task without removing it.

        Time complexity:
            O(1)
        """
        if self.is_empty():
            return None

        return self.heap[0]

    def extract_max(self):
        """
        Remove and return the task with the highest priority.

        Time complexity:
            O(log n)
        """
        if self.is_empty():
            return None

        maximum = self.heap[0]
        last_task = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last_task
            self._heapify_down(0)

        return maximum

    def _find_task_index(self, task_id):
        """
        Find the index of a task by its identifier.

        This implementation uses a linear search, so lookup is O(n).
        """
        for index, task in enumerate(self.heap):
            if task.task_id == task_id:
                return index

        return -1

    def increase_key(self, task_id, new_priority):
        """
        Increase the priority of an existing task.

        Returns:
            True if the priority was updated.
            False if the task was not found.

        Raises:
            ValueError if the new priority is smaller than the
            current priority.
        """
        index = self._find_task_index(task_id)

        if index == -1:
            return False

        if new_priority < self.heap[index].priority:
            raise ValueError(
                "New priority must be greater than or equal "
                "to the current priority."
            )

        self.heap[index].priority = new_priority
        self._heapify_up(index)

        return True

    def display(self):
        """Display the current binary heap."""
        if self.is_empty():
            print("Priority queue is empty.")
            return

        for index, task in enumerate(self.heap):
            print(f"Heap index {index}: {task}")


def main():
    """
    Demonstrate and test the max-priority queue implementation.
    """
    print("Max-Priority Queue Implementation Tests")
    print("=" * 60)

    queue = MaxPriorityQueue()

    # Test 1: Empty queue
    print("\nTest 1 - Empty queue")
    print(f"is_empty(): {queue.is_empty()}")
    print(f"extract_max(): {queue.extract_max()}")
    print(f"peek_max(): {queue.peek_max()}")

    # Test 2: Insert tasks
    print("\nTest 2 - Insert tasks")

    tasks = [
        Task(1, "Process laboratory results", 4),
        Task(2, "Handle urgent system alert", 10),
        Task(3, "Generate daily report", 2),
        Task(4, "Process integration message", 7),
        Task(5, "Run scheduled backup", 3),
    ]

    for task in tasks:
        print(f"Inserting: {task}")
        queue.insert(task)

    print("\nHeap after insertions:")
    queue.display()

    print(f"\nis_empty(): {queue.is_empty()}")
    print(f"Highest-priority task: {queue.peek_max()}")

    # Test 3: Increase priority
    print("\nTest 3 - Increase key")

    print("Increasing Task 3 priority from 2 to 12.")
    updated = queue.increase_key(3, 12)

    print(f"Update successful: {updated}")
    print(f"Highest-priority task after update: {queue.peek_max()}")

    print("\nHeap after increase_key:")
    queue.display()

    # Test 4: Missing task
    print("\nTest 4 - Increase priority of missing task")
    updated = queue.increase_key(99, 20)
    print(f"Update successful: {updated}")

    # Test 5: Invalid priority decrease
    print("\nTest 5 - Reject an invalid priority decrease")

    try:
        queue.increase_key(2, 1)
    except ValueError as error:
        print(f"Correctly rejected: {error}")

    # Test 6: Extract tasks
    print("\nTest 6 - Extract tasks in priority order")

    extracted_priorities = []

    while not queue.is_empty():
        task = queue.extract_max()
        extracted_priorities.append(task.priority)
        print(f"Extracted: {task}")

    expected_priorities = sorted(
        [4, 10, 12, 7, 3],
        reverse=True,
    )

    print(f"\nExtracted priorities: {extracted_priorities}")
    print(f"Expected priorities:  {expected_priorities}")
    print(
        "Priority-order test passed: "
        f"{extracted_priorities == expected_priorities}"
    )

    # Test 7: Queue after removing everything
    print("\nTest 7 - Queue after all extractions")
    print(f"is_empty(): {queue.is_empty()}")
    print(f"extract_max(): {queue.extract_max()}")

    # Test 8: Single task
    print("\nTest 8 - Single-task queue")

    queue.insert(Task(6, "Single task", 5))

    print(f"Inserted: {queue.peek_max()}")
    print(f"Extracted: {queue.extract_max()}")
    print(f"is_empty(): {queue.is_empty()}")

    # Test 9: Duplicate priorities
    print("\nTest 9 - Duplicate priorities")

    duplicate_queue = MaxPriorityQueue()

    duplicate_queue.insert(Task(7, "Task A", 5))
    duplicate_queue.insert(Task(8, "Task B", 5))
    duplicate_queue.insert(Task(9, "Task C", 5))

    duplicate_results = []

    while not duplicate_queue.is_empty():
        duplicate_results.append(
            duplicate_queue.extract_max().priority
        )

    print(f"Extracted priorities: {duplicate_results}")
    print(
        "Duplicate-priority test passed: "
        f"{duplicate_results == [5, 5, 5]}"
    )

    print("\n" + "=" * 60)
    print("All Priority Queue tests completed.")


if __name__ == "__main__":
    main()