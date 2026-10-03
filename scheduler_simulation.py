"""
Assignment 4: Heap Data Structures
Priority Queue Scheduling Simulation

This program demonstrates a practical application of the binary-heap
priority queue. Tasks are inserted with different priorities, and the
scheduler processes the highest-priority task first.
"""

from priority_queue import Task, MaxPriorityQueue


def display_task_list(tasks):
    """
    Display the tasks before they are added to the scheduler.
    """
    print("\nTasks submitted to the scheduler:")
    print("-" * 75)

    for task in tasks:
        print(
            f"Task ID: {task.task_id:<2} | "
            f"Priority: {task.priority:<2} | "
            f"Description: {task.description}"
        )


def run_scheduler(tasks):
    """
    Insert tasks into a max-priority queue and process them
    from highest to lowest priority.

    Returns:
        list: Tasks in the order in which they were processed.
    """
    queue = MaxPriorityQueue()

    print("\nAdding tasks to the priority queue...")
    print("-" * 75)

    for task in tasks:
        queue.insert(task)
        print(
            f"Added Task {task.task_id}: "
            f"{task.description} "
            f"(priority={task.priority})"
        )

    print("\nProcessing tasks:")
    print("-" * 75)

    processed_tasks = []
    execution_number = 1

    while not queue.is_empty():
        task = queue.extract_max()
        processed_tasks.append(task)

        print(
            f"{execution_number}. "
            f"Task {task.task_id} | "
            f"Priority {task.priority} | "
            f"{task.description}"
        )

        execution_number += 1

    return processed_tasks


def verify_schedule(processed_tasks):
    """
    Verify that tasks were processed in non-increasing
    priority order.
    """
    priorities = [task.priority for task in processed_tasks]

    expected = sorted(priorities, reverse=True)

    print("\nSchedule Verification")
    print("-" * 75)
    print(f"Processed priorities: {priorities}")
    print(f"Expected priorities:  {expected}")
    print(f"Correct priority order: {priorities == expected}")

    return priorities == expected


def demonstrate_dynamic_priority():
    """
    Demonstrate how a task can become more urgent after
    it has already been placed in the scheduler.
    """
    print("\nDynamic Priority Update Demonstration")
    print("-" * 75)

    queue = MaxPriorityQueue()

    tasks = [
        Task(101, "Generate routine report", 2),
        Task(102, "Process standard integration request", 5),
        Task(103, "Review application log", 3),
    ]

    for task in tasks:
        queue.insert(task)

    print(f"Initially highest priority: {queue.peek_max()}")

    print(
        "\nA production issue makes Task 101 urgent. "
        "Its priority is increased from 2 to 10."
    )

    queue.increase_key(101, 10)

    print(f"Highest priority after update: {queue.peek_max()}")

    updated_order = []

    while not queue.is_empty():
        updated_order.append(queue.extract_max())

    print("\nProcessing order after priority update:")

    for position, task in enumerate(updated_order, start=1):
        print(
            f"{position}. Task {task.task_id} | "
            f"Priority {task.priority} | "
            f"{task.description}"
        )

    priorities = [task.priority for task in updated_order]

    print(
        "Dynamic-priority test passed: "
        f"{priorities == sorted(priorities, reverse=True)}"
    )


def main():
    """
    Run the scheduling simulation and verification tests.
    """
    print("Priority Queue Task Scheduling Simulation")
    print("=" * 75)

    tasks = [
        Task(
            1,
            "Generate routine daily report",
            2
        ),
        Task(
            2,
            "Process integration message",
            6
        ),
        Task(
            3,
            "Handle critical system alert",
            10
        ),
        Task(
            4,
            "Run scheduled backup",
            3
        ),
        Task(
            5,
            "Process high-priority data request",
            8
        ),
        Task(
            6,
            "Perform routine log review",
            1
        ),
        Task(
            7,
            "Resolve application processing error",
            7
        ),
    ]

    display_task_list(tasks)

    processed_tasks = run_scheduler(tasks)

    schedule_correct = verify_schedule(processed_tasks)

    print("\nScheduling Result")
    print("-" * 75)

    if schedule_correct:
        print(
            "PASS: The scheduler processed all tasks "
            "from highest to lowest priority."
        )
    else:
        print(
            "FAIL: The scheduler did not process tasks "
            "in the expected priority order."
        )

    demonstrate_dynamic_priority()

    print("\n" + "=" * 75)
    print("Scheduler simulation completed.")


if __name__ == "__main__":
    main()