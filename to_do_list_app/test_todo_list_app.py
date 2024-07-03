import unittest
from unittest.mock import patch, call
from todo_list_app import Task, Event, TodoList, get_time_input, get_date_input, get_valid_item_id

class TestTodoListApp(unittest.TestCase):

    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        task = Task("Test Task")
        self.todo_list.add_item(task)
        self.assertEqual(len(self.todo_list.items), 1)
        self.assertIsInstance(self.todo_list.items[0][1], Task)
        self.assertEqual(self.todo_list.items[0][1].description, "Test Task")

    def test_add_event(self):
        event = Event("Test Event", "2024-06-27", "10:00 AM", "11:00 AM")
        self.todo_list.add_item(event)
        self.assertEqual(len(self.todo_list.items), 1)
        self.assertIsInstance(self.todo_list.items[0][1], Event)
        self.assertEqual(self.todo_list.items[0][1].description, "Test Event")
        self.assertEqual(self.todo_list.items[0][1].event_date, "2024-06-27")
        self.assertEqual(self.todo_list.items[0][1].start_time, "10:00 AM")
        self.assertEqual(self.todo_list.items[0][1].end_time, "11:00 AM")

    def test_delete_item(self):
        task = Task("Test Task")
        self.todo_list.add_item(task)
        task_id = self.todo_list.items[0][0]
        self.todo_list.delete_item(task_id)
        self.assertEqual(len(self.todo_list.items), 0)

    def test_delete_item_invalid_id(self):
        task = Task("Test Task")
        self.todo_list.add_item(task)
        invalid_id = 999
        with patch('builtins.print') as mock_print:
            self.todo_list.delete_item(invalid_id)
            mock_print.assert_called_with(f"No item found with ID {invalid_id}")

    def test_show_items(self):
        task = Task("Test Task")
        self.todo_list.add_item(task)
        with patch('builtins.print') as mock_print:
            self.todo_list.show_items()
            mock_print.assert_has_calls([
                call("Todo List Items:"),
                call(f"ID: 1, {task}")
            ])

    def test_show_items_empty(self):
        with patch('builtins.print') as mock_print:
            self.todo_list.show_items()
            mock_print.assert_called_with("No items in the list.")

    def test_mark_as_completed(self):
        task = Task("Test Task")
        self.todo_list.add_item(task)
        task_id = self.todo_list.items[0][0]
        self.todo_list.mark_as_completed(task_id)
        self.assertTrue(self.todo_list.items[0][1].completed)

    def test_mark_as_completed_invalid_id(self):
        with patch('builtins.print') as mock_print:
            self.todo_list.mark_as_completed(1)
            mock_print.assert_called_with("No item found with ID 1")

    def test_get_time_input_valid(self):
        with patch('builtins.input', return_value='10:00 AM'):
            self.assertEqual(get_time_input("Enter time: "), '10:00 AM')

    def test_get_time_input_invalid(self):
        with patch('builtins.input', side_effect=['invalid', '10:00 AM']):
            with patch('builtins.print') as mock_print:
                self.assertEqual(get_time_input("Enter time: "), '10:00 AM')
                mock_print.assert_called_with("Invalid time format. Please enter time in HH:MM AM/PM format.")

    def test_get_date_input_valid(self):
        with patch('builtins.input', return_value='2024-06-27'):
            self.assertEqual(get_date_input("Enter date: "), '2024-06-27')

    def test_get_date_input_invalid(self):
        with patch('builtins.input', side_effect=['invalid', '2024-06-27']):
            with patch('builtins.print') as mock_print:
                self.assertEqual(get_date_input("Enter date: "), '2024-06-27')
                mock_print.assert_called_with("Invalid date format. Please enter date in YYYY-MM-DD format.")

    def test_get_valid_item_id_valid(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(get_valid_item_id("Enter item ID: "), 1)

    def test_get_valid_item_id_invalid(self):
        with patch('builtins.input', side_effect=['invalid', '-1', '1']):
            with patch('builtins.print') as mock_print:
                self.assertEqual(get_valid_item_id("Enter item ID: "), 1)
                mock_print.assert_has_calls([
                    call("Error: Invalid input. Please enter a positive integer."),
                    call("Error: Item ID must be a positive integer.")
                ])      
if __name__ == '__main__':
    unittest.main()