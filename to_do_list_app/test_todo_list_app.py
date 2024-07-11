import unittest
from unittest.mock import patch, call
from todo_list_app import Item, Task, Event, TodoList, get_time_input, get_date_input, get_valid_item_id

class TestTodoListApp(unittest.TestCase):
    """
    This class tests the functionalities of the TodoList application, 
    including adding tasks and events, deleting items, showing items, 
    marking items as completed, and handling input validation.
    """

    def setUp(self):
        """Sets up a new TodoList instance before each test."""
        self.todo_list = TodoList()

    def test_item_str(self):
        """
        This test checks if the string representation of an Item is correctly 
        formatted and reflects the completed status.
        """
        item = Item("Test Item") # Creates a new Item
        self.assertEqual(str(item), "Item: Test Item, Status: Not Completed") # Checks if the string representation is correct for not completed item
        item.mark_as_completed() # Marks the item as completed
        self.assertEqual(str(item), "Item: Test Item, Status: Completed") # Checks if the string representation is correct for completed item

    def test_event_str(self):
        """
        This test checks if the string representation of an Event is correctly 
        formatted and reflects the completed status.
        """
        event = Event("Test Event", "2024-06-27", "10:00 AM", "11:00 AM") # Creates a new Event
        self.assertEqual(str(event), "Event: Test Event, Date: 2024-06-27, Time: 10:00 AM - 11:00 AM, Status: Not Completed") # Checks if the string representation is correct for not completed event
        event.mark_as_completed() # Marks the event as completed
        self.assertEqual(str(event), "Event: Test Event, Date: 2024-06-27, Time: 10:00 AM - 11:00 AM, Status: Completed") # Checks if the string representation is correct for completed event

    def test_add_task(self):
        """
        This test checks if a task can be added to the todo list and verifies 
        the task's attributes.
        """
        task = Task("Test Task") # Creates a new Task
        self.todo_list.add_item(task)  # Adds the task to the todo list
        self.assertEqual(len(self.todo_list.items), 1) # Checks if the todo list has one item
        self.assertIsInstance(self.todo_list.items[0][1], Task) # Checks if the first item in the list is a Task
        self.assertEqual(self.todo_list.items[0][1].description, "Test Task")  # Checks if the task's description is correct

    def test_add_event(self):
        """
        This test checks if an event can be added to the todo list and verifies 
        the event's attributes, including date and time input validation.
        """
        # Mocks user input for a valid date
        with patch('builtins.input', return_value='2024-06-27'):
            event_date = get_date_input("Enter date: ")
            self.assertEqual(event_date, '2024-06-27') # Checks if the date input is correct
        
        # Mocks user input for an invalid date followed by a valid date
        with patch('builtins.input', side_effect=['invalid', '2024-06-27']):
            with patch('builtins.print') as mock_print:
                event_date = get_date_input("Enter date: ")
                self.assertEqual(event_date, '2024-06-27') # Checks if the date input is corrected to the valid date
                mock_print.assert_called_with("Invalid date format. Please enter date in YYYY-MM-DD format.") # Checks if the correct error message is printed
        
        # Mocks user input for a valid start time
        with patch('builtins.input', return_value='10:00 AM'):
            start_time = get_time_input("Enter start time: ")
            self.assertEqual(start_time, '10:00 AM') # Checks if the start time input is correct
        
        # Mocks user input for an invalid start time followed by a valid start time
        with patch('builtins.input', side_effect=['invalid', '10:00 AM']):
            with patch('builtins.print') as mock_print:
                start_time = get_time_input("Enter start time: ")
                self.assertEqual(start_time, '10:00 AM') # Checks if the start time input is corrected to the valid start time
                mock_print.assert_called_with("Invalid time format. Please enter time in HH:MM AM/PM format.") # Checks if the correct error message is printed
        
        end_time = '11:00 AM' # Defines the end time
        event = Event("Test Event", event_date, start_time, end_time) # Creates a new Event
        self.todo_list.add_item(event) # Adds the event to the todo list
        self.assertEqual(len(self.todo_list.items), 1) # Checks if the todo list has one item
        self.assertIsInstance(self.todo_list.items[0][1], Event) # Checks if the first item in the list is an Event
        self.assertEqual(self.todo_list.items[0][1].description, "Test Event") # Checks if the event's description is correct
        self.assertEqual(self.todo_list.items[0][1].event_date, "2024-06-27") # Checks if the event's date is correct
        self.assertEqual(self.todo_list.items[0][1].start_time, "10:00 AM") # Checks if the event's start time is correct
        self.assertEqual(self.todo_list.items[0][1].end_time, "11:00 AM") # Checks if the event's end time is correct

    def test_delete_item(self):
        """
        This test checks if an item can be deleted from the todo list using a 
        valid ID and verifies the error handling for an invalid ID.
        """
        task = Task("Test Task") # Creates a new Task
        self.todo_list.add_item(task) # Creates a new Task
        task_id = self.todo_list.items[0][0] # Gets the ID of the task
        
        # Mocks user input for a valid item ID
        with patch('builtins.input', return_value=str(task_id)):
            valid_item_id = get_valid_item_id("Enter item ID: ")
            self.assertEqual(valid_item_id, task_id) # Checks if the valid item ID input is correct
        
        # Mocks user input for invalid item IDs followed by a valid item ID
        with patch('builtins.input', side_effect=['invalid', '-1', str(task_id)]):
            with patch('builtins.print') as mock_print:
                valid_item_id = get_valid_item_id("Enter item ID: ")
                self.assertEqual(valid_item_id, task_id) # Checks if the valid item ID input is correct
                # Checks if the correct error messages are printed
                mock_print.assert_has_calls([
                    call("Error: Invalid input. Please enter a positive integer."),
                    call("Error: Item ID must be a positive integer.")
                ])
        
        self.todo_list.delete_item(valid_item_id)  # Deletes the item with the valid ID
        self.assertEqual(len(self.todo_list.items), 0) # Checks if the todo list is empty
        
        invalid_id = 999 # Defines an invalid ID
        # Mocks print to capture the output
        with patch('builtins.print') as mock_print:
            self.todo_list.delete_item(invalid_id)
            mock_print.assert_called_with("Error: There are no items to delete.")# Checks if the correct error message is printed

    def test_show_items(self):
        """
        This test checks if the todo list items can be displayed and verifies 
        the message when the list is empty.
        """
        task = Task("Test Task") # Creates a new Task
        self.todo_list.add_item(task) # Adds the task to the todo list
        # Mocks print to capture the output
        with patch('builtins.print') as mock_print:
            self.todo_list.show_items()
            # Checks if the correct items are printed
            mock_print.assert_has_calls([
                call("Todo List Items:"),
                call(f"ID: 1, {task}")
            ])
        
        self.todo_list.items.clear() # Clears the todo list
        # Mocks print to capture the output
        with patch('builtins.print') as mock_print:
            self.todo_list.show_items()
            mock_print.assert_called_with("No items in the list.") # Checks if the correct message is printed for an empty list

    def test_mark_as_completed(self):
        """
        This test checks if an item can be marked as completed using a valid ID 
        and verifies the error handling for an invalid ID.
        """
        task = Task("Test Task") # Creates a new Task
        self.todo_list.add_item(task) # Adds the task to the todo list
        task_id = self.todo_list.items[0][0] # Gets the ID of the task
        
        # Mocks user input for a valid item ID
        with patch('builtins.input', return_value=str(task_id)):
            valid_item_id = get_valid_item_id("Enter item ID: ")
            self.assertEqual(valid_item_id, task_id) # Checks if the valid item ID input is correct
        
        self.todo_list.mark_as_completed(valid_item_id) # Marks the item as completed with the valid ID
        self.assertTrue(self.todo_list.items[0][1].completed) # Checks if the item is marked as completed
        
        # Mocks print to capture the output
        with patch('builtins.print') as mock_print:
            self.todo_list.mark_as_completed(999)
            mock_print.assert_called_with("No item found with ID 999") # Checks if the correct error message is printed for an invalid ID
    
if __name__ == '__main__':
    unittest.main()