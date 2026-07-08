# Specification: Task Management

## Objective
The system must allow a user to manage their daily tasks, including the possibility of assigning an optional due date to each task.

## Functional Requirements
1. **Create a task**: The user can create a task with a title, an optional description, a status (Pending by default), and an optional due date.
2. **Save the due date**: If a due date is provided, the system must store it along with the task in a valid date format.
3. **Complete a task**: The user can mark a task as "Completed".
4. **List tasks**: The system can return all tasks, optionally filtering by status and showing the due date when it exists.
5. **Identify overdue tasks**: The system must allow visual identification or through an attribute that a task is overdue when its due date has passed and the task is still pending.
6. **Identify tasks about to expire**: The system must be able to filter pending tasks that have an upcoming due date, for example within a configurable range of days.
7. **Filter by year**: The system must allow filtering and returning all tasks created in a specific year provided by the user.
8. **Filter by month**: The system must allow filtering and returning all tasks created in a specific month, expressed as a number from 1 to 12.
9. **Limit title length**: The title of a task must not exceed 50 characters. If a user attempts to create a task with a longer title, the system must reject it with an error.
10. **Validate date range**: The due date of a task cannot be earlier than the year 1950. If an earlier date is provided, the system must reject it with an error.
11. **Assign categories to a task**: The system must allow assigning an optional category to each task, represented by a non-empty text string.
12. **Filter tasks by category**: The system must allow returning only the tasks that belong to a specific category.
13. **Support subcategories**: Each category can have an optional subcategory, also represented by a non-empty text string. The task must store the category and the subcategory independently.
14. **Filter tasks by subcategory**: The system must allow returning only the tasks that belong to a specific subcategory.
15. **Filter by month and year**: The system must allow filtering tasks by month and year at the same time.

## Expected Behavior
- If the title is empty, the system must raise a `ValueError`.
- If the title exceeds 50 characters, the system must raise a `ValueError`.
- If a due date is provided, it must be a valid date; otherwise, the system must raise a `ValueError`.
- If the due date is earlier than 1950-01-01, the system must raise a `ValueError`.
- If the category is provided, it must be a non-empty string; otherwise, the system must raise a `ValueError`.
- If the subcategory is provided, it must be a non-empty string; otherwise, the system must raise a `ValueError`.
- If no due date is provided, the task must be saved without it and continue to function normally.
- When completing a task, its status changes and the update date is recorded.
- A pending task with a past due date must be considered overdue.
- A pending task with a due date within the configured range must be considered about to expire.
- Completed tasks or tasks without a due date must not appear in the "about to expire" filter.
- When filtering by year, if no task matches, an empty list is returned. The year must be an integer (e.g. 2026).
- When filtering by month, if the value is invalid (outside 1 to 12), the system must raise a `ValueError`.
- When filtering by month, if no task matches, an empty list is returned.
- When filtering by category, if no task matches, an empty list is returned.
- When filtering by subcategory, if no task matches, an empty list is returned.
