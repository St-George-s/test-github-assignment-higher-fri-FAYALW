from taskNode import TaskNode
from taskList import TaskList

tasks = TaskList()
tasks.add_task("Maths", "Finish worksheet", "2025-06-20")
tasks.add_task("English", "Read Chapter 5", "2025-06-19")
tasks.add_task("History", "Complete textbook questions", "2025-06-18")
tasks.complete_task()
tasks.complete_task()
tasks.complete_task()
tasks.print_tasks()