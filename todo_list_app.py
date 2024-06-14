# Defining Class Task
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task: {self.description}, Status: {status}"

# Defining Class TodoList
class TodoList:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1
        
    # defining add_task method
    def add_task(self, description):
        task = Task(description)
        self.tasks.append((self.task_id_counter, task))
        print(f"Success: Task added with ID {self.task_id_counter}: {description}")
        self.task_id_counter += 1

    # defining delete_task method
    def delete_task(self, task_id):
        for index, (task_id_, task) in enumerate(self.tasks):
            if task_id_ == task_id:
                del self.tasks[index]
                print(f"Deleted task with ID {task_id}")
                break
        else:
            print(f"No task found with ID {task_id}")

    # defining show_tasks method
    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Todo List Tasks:")
            for task_id, task in self.tasks:
                print(f"ID: {task_id}, {task}")

    # defining mark_as_completed method
    def mark_as_completed(self, task_id):
        for task_id_, task in self.tasks:
            if task_id_ == task_id:
                task.mark_as_completed()
                print(f"Task with ID {task_id} is marked as completed")
                break
        else:
            print(f"No task found with ID {task_id}")

def main():
    
    # Creating TodoList Object
    todo_list = TodoList()
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            task_id = int(input("Enter the task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            task_id = int(input("Enter the task ID to mark as completed: "))
            todo_list.mark_as_completed(task_id)
        elif choice == '5':
            print("Exiting the Todo List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()