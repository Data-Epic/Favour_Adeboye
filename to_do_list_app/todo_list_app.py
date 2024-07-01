from datetime import datetime

# Base Class
class Item:
    """
    This is a base class representing a generic item in the todo list.
    
    Attributes:
        description (str): The description of the item.
        completed (bool): A flag indicating whether the item is completed or not.
    """
    
    def __init__(self, description):
        """
        Initializes the item with a description.
        
        Argument:
            description (str): The description of the item.
        """
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        """
        Marks the item as completed.
        """
        self.completed = True

    def __str__(self):
        """
        Returns a string representation of the item.
        
        Returns:
            str: A string representing the item, including its type, description, and completion status.
        """
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.__class__.__name__}: {self.description}, Status: {status}"

# Derived Class for Task
class Task(Item):
    """
    A child class representing a task in the todo list, derived from the Item class.
    """
    
    def __init__(self, description):
        """
        Initializes the task with a description.
        
        Argument:
            description (str): The description of the task.
        """
        super().__init__(description)

# Derived Class for Event
class Event(Item):
    """
    Another class representing an event in the todo list, derived from the Item class.
    
    Attributes:
        event_date (str): The date of the event.
        start_time (str): The start time of the event.
        end_time (str): The end time of the event.
    """
    
    def __init__(self, description, event_date, start_time, end_time):
        """
        Initializes the event with a description, date, start time, and end time.
        
        Argument:
            description (str): The description of the event.
            event_date (str): The date of the event in YYYY-MM-DD format.
            start_time (str): The start time of the event in HH:MM AM/PM format.
            end_time (str): The end time of the event in HH:MM AM/PM format.
        """
        super().__init__(description)
        self.event_date = event_date
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        """
        Returns a string representation of the event.
        
        Returns:
            str: A string representing the event, including its description, date, time, and completion status.
        """
        status = "Completed" if self.completed else "Not Completed"
        return (f"Event: {self.description}, Date: {self.event_date}, "
                f"Time: {self.start_time} - {self.end_time}, Status: {status}")

# TodoList Class
class TodoList:
    """
    A class representing a todo list that can contain both tasks and events.
    
    Attributes:
        items (list): A list of tuples containing item IDs and items.
        item_id_counter (int): A counter for generating unique item IDs.
    """
    
    def __init__(self):
        """
        Initializes the todo list with an empty list of items and an item ID counter starting at 1.
        """
        self.items = []
        self.item_id_counter = 1
        
    def add_item(self, item):
        """
        Adds an item to the todo list and assign it a unique ID.
        
        Argument:
            item (Item): The item to add to the list.
        """
        self.items.append((self.item_id_counter, item))
        if isinstance(item, Event):
            print(f"Success: Event added with ID {self.item_id_counter}: {item.description}, Date: {item.event_date}, "
                  f"Time: {item.start_time} - {item.end_time}")
        else:
            print(f"Success: Task added with ID {self.item_id_counter}: {item.description}")
        self.item_id_counter += 1

    def delete_item(self, item_id):
        """
        Deletes an item from the todo list by its ID.
        
        Argument:
            item_id (int): The ID of the item to delete.
        """
        if not self.items:
            print("Error: There are no items to delete.")
            return
        
        for index, (item_id_, item) in enumerate(self.items):
            if item_id_ == item_id:
                del self.items[index]
                print(f"Deleted {item.__class__.__name__} with ID {item_id}")
                break
        else:
            print(f"No item found with ID {item_id}")

    def show_items(self):
        """
        Displays all items in the todo list.
        """
        if not self.items:
            print("No items in the list.")
        else:
            print("Todo List Items:")
            for item_id, item in self.items:
                print(f"ID: {item_id}, {item}")

    def mark_as_completed(self, item_id):
        """
        Marks an item in the todo list as completed by its ID.
        
        Argument:
            item_id (int): The ID of the item to mark as completed.
        """
        for item_id_, item in self.items:
            if item_id_ == item_id:
                item.mark_as_completed()
                print(f"{item.__class__.__name__} with ID {item_id} is marked as completed")
                break
        else:
            print(f"No item found with ID {item_id}")

def get_time_input(prompt):
    """
    Prompts the user for a time input and validate the format.
    
    Argument:
        prompt (str): The input prompt for the user.
        
    Returns:
        str: The validated time in HH:MM AM/PM format.
    """
    while True:
        try:
            time_str = input(prompt)
            time_obj = datetime.strptime(time_str, '%I:%M %p')
            return time_obj.strftime('%I:%M %p')
        except ValueError:
            print("Invalid time format. Please enter time in HH:MM AM/PM format.")

def get_date_input(prompt):
    """
    Prompts the user for a date input and validate the format.
    
    Argument:
        prompt (str): The input prompt for the user.
        
    Returns:
        str: The validated date in YYYY-MM-DD format.
    """
    while True:
        try:
            date_str = input(prompt)
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")

def get_valid_item_id(prompt):
    """
    Prompts the user for an item ID and validate the input.
    
    Argument:
        prompt (str): The input prompt for the user.
        
    Returns:
        int: The validated item ID.
    """
    while True:
        try:
            item_id = int(input(prompt))
            if item_id > 0:
                return item_id
            else:
                print("Error: Item ID must be a positive integer.")
        except ValueError:
            print("Error: Invalid input. Please enter a positive integer.")

def main():
    """
    This is the main function to run the todo list application, by providing a menu for the user to interact with.
    """
    todo_list = TodoList()
    
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Add Event")
        print("3. Delete Item")
        print("4. Show Items")
        print("5. Mark Item as Completed")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            description = input("Enter the task description: ")
            task = Task(description)
            todo_list.add_item(task)
        elif choice == '2':
            description = input("Enter the event description: ")
            event_date = get_date_input("Enter the event date (YYYY-MM-DD): ")
            while True:
                start_time = get_time_input("Enter the start time (HH:MM AM/PM): ")
                end_time = get_time_input("Enter the end time (HH:MM AM/PM): ")
                if datetime.strptime(start_time, '%I:%M %p') < datetime.strptime(end_time, '%I:%M %p'):
                    break
                else:
                    print("Start time cannot be after end time. Please enter the times again.")
            event = Event(description, event_date, start_time, end_time)
            todo_list.add_item(event)
        elif choice == '3':
            if not todo_list.items:
                print("Error: There are no items to delete.")
            else:
                item_id = get_valid_item_id("Enter the item ID to delete: ")
                todo_list.delete_item(item_id)
        elif choice == '4':
            todo_list.show_items()
        elif choice == '5':
            item_id = get_valid_item_id("Enter the item ID to mark as completed: ")
            todo_list.mark_as_completed(item_id)
        elif choice == '6':
            print("Exiting the Todo List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()