import unittest
from unittest.mock import patch, call
from todo_list_app import Task, Event, TodoList, get_time_input, get_date_input, get_valid_item_id

class TestTodoListApp(unittest.TestCase):
    """
    Unit test class for testing the Todo List application.
    """

    def setUp(self):
        """
        Sets up a new TodoList instance before each test.
        """
        self.todo_list = TodoList()  # Initialize a new TodoList object for each test

    def test_add_task(self):
        """
        Tests adding a task to the todo list.
        """
        task = Task("Test Task")  # Create a new Task object
        self.todo_list.add_item(task)  # Add the task to the todo list
        self.assertEqual(len(self.todo_list.items), 1)  # Check that the list contains one item
        self.assertIsInstance(self.todo_list.items[0][1], Task)  # Check that the item is a Task
        self.assertEqual(self.todo_list.items[0][1].description, "Test Task")  # Check the task description

    def test_add_event(self):
        """
        Tests adding an event to the todo list.
        """
        event = Event("Test Event", "2024-06-27", "10:00 AM", "11:00 AM")  # Create a new Event object
        self.todo_list.add_item(event)  # Add the event to the todo list
        self.assertEqual(len(self.todo_list.items), 1)  # Check that the list contains one item
        self.assertIsInstance(self.todo_list.items[0][1], Event)  # Check that the item is an Event
        self.assertEqual(self.todo_list.items[0][1].description, "Test Event")  # Check the event description
        self.assertEqual(self.todo_list.items[0][1].event_date, "2024-06-27")  # Check the event date
        self.assertEqual(self.todo_list.items[0][1].start_time, "10:00 AM")  # Check the start time
        self.assertEqual(self.todo_list.items[0][1].end_time, "11:00 AM")  # Check the end time

    def test_delete_item(self):
        """
        Tests deleting an item from the todo list by its ID.
        """
        task = Task("Test Task")  # Create a new Task object
        self.todo_list.add_item(task)  # Add the task to the todo list
        task_id = self.todo_list.items[0][0]  # Get the ID of the task
        self.todo_list.delete_item(task_id)  # Delete the task by its ID
        self.assertEqual(len(self.todo_list.items), 0)  # Check that the list is now empty

    def test_delete_item_invalid_id(self):
        """
        Tests deleting an item with an invalid ID.
        """
        task = Task("Test Task")  # Create a new Task object
        self.todo_list.add_item(task)  # Add the task to the todo list
        invalid_id = 999  # Define an invalid ID
        with patch('builtins.print') as mock_print:  # Mock the print function
            self.todo_list.delete_item(invalid_id)  # Attempt to delete the item with an invalid ID
            mock_print.assert_called_with(f"No item found with ID {invalid_id}")  # Check that the correct message is printed

    def test_show_items(self):
        """
        Tests showing all items in the todo list.
        """
        task = Task("Test Task")  # Create a new Task object
        self.todo_list.add_item(task)  # Add the task to the todo list
        with patch('builtins.print') as mock_print:  # Mock the print function
            self.todo_list.show_items()  # Show the items in the todo list
            mock_print.assert_has_calls([
                call("Todo List Items:"),
                call(f"ID: 1, {task}")
            ])  # Check that the correct messages are printed

    def test_show_items_empty(self):
        """
        Tests showing items when the todo list is empty.
        """
        with patch('builtins.print') as mock_print:  # Mock the print function
            self.todo_list.show_items()  # Show the items in the todo list
            mock_print.assert_called_with("No items in the list.")  # Check that the correct message is printed

    def test_mark_as_completed(self):
        """
        Tests marking an item as completed.
        """
        task = Task("Test Task")  # Create a new Task object
        self.todo_list.add_item(task)  # Add the task to the todo list
        task_id = self.todo_list.items[0][0]  # Get the ID of the task
        self.todo_list.mark_as_completed(task_id)  # Mark the task as completed
        self.assertTrue(self.todo_list.items[0][1].completed)  # Check that the task is marked as completed

    def test_mark_as_completed_invalid_id(self):
        """
        Tests marking an item as completed with an invalid ID.
        """
        with patch('builtins.print') as mock_print:  # Mock the print function
            self.todo_list.mark_as_completed(1)  # Attempt to mark an item with an invalid ID as completed
            mock_print.assert_called_with("No item found with ID 1")  # Check that the correct message is printed

    def test_get_time_input_valid(self):
        """
        Tests getting a valid time input.
        """
        with patch('builtins.input', return_value='10:00 AM'):  # Mock the input function to return a valid time
            self.assertEqual(get_time_input("Enter time: "), '10:00 AM')  # Check that the function returns the correct time

    def test_get_time_input_invalid(self):
        """
        Tests getting an invalid time input and then a valid time input.
        """
        with patch('builtins.input', side_effect=['invalid', '10:00 AM']):  # Mock the input function to first return an invalid time and then a valid time
            with patch('builtins.print') as mock_print:  # Mock the print function
                self.assertEqual(get_time_input("Enter time: "), '10:00 AM')  # Check that the function eventually returns the correct time
                mock_print.assert_called_with("Invalid time format. Please enter time in HH:MM AM/PM format.")  # Check that the correct error message is printed

    def test_get_date_input_valid(self):
        """
        Tests getting a valid date input.
        """
        with patch('builtins.input', return_value='2024-06-27'):  # Mock the input function to return a valid date
            self.assertEqual(get_date_input("Enter date: "), '2024-06-27')  # Check that the function returns the correct date

    def test_get_date_input_invalid(self):
        """
        Tests getting an invalid date input and then a valid date input.
        """
        with patch('builtins.input', side_effect=['invalid', '2024-06-27']):  # Mock the input function to first return an invalid date and then a valid date
            with patch('builtins.print') as mock_print:  # Mock the print function
                self.assertEqual(get_date_input("Enter date: "), '2024-06-27')  # Check that the function eventually returns the correct date
                mock_print.assert_called_with("Invalid date format. Please enter date in YYYY-MM-DD format.")  # Check that the correct error message is printed

    def test_get_valid_item_id_valid(self):
        """
        Tests getting a valid item ID.
        """
        with patch('builtins.input', return_value='1'):  # Mock the input function to return a valid item ID
            self.assertEqual(get_valid_item_id("Enter item ID: "), 1)  # Check that the function returns the correct item ID

    def test_get_valid_item_id_invalid(self):
        """
        Tests getting invalid item IDs and then a valid item ID.
        """
        with patch('builtins.input', side_effect=['invalid', '-1', '1']):  # Mock the input function to return invalid item IDs and then a valid item ID
            with patch('builtins.print') as mock_print:  # Mock the print function
                self.assertEqual(get_valid_item_id("Enter item ID: "), 1)  # Check that the function eventually returns the correct item ID
                mock_print.assert_has_calls([
                    call("Error: Invalid input. Please enter a positive integer."),
                    call("Error: Item ID must be a positive integer.")
                ])  # Check that the correct error messages are printed

if __name__ == '__main__':
    unittest.main()  # Run the unit tests if the script is executed directly
