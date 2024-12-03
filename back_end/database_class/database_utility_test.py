import database_utility_class as dbu
import unittest
from unittest.mock import MagicMock


class database_utility_test(unittest.TestCase):
    
    def setUp(self):
        # Set up mock cursor and database connection
        self.mock_cursor = MagicMock()
        self.mock_db = MagicMock()

        # Assign the mock cursor and database to the global variables in dbu
        dbu.mycursor = self.mock_cursor
        dbu.mydb = self.mock_db
    
    def test_get_active_inventory(self):
        # Mock the data returned from the database
        mock_data = [
            (1, '1HGCM82633A123456', 30000, 30, 25000, 'ABC123', '2020', 'Civic', 'Honda', 'Blue', 'Sedan', 1),
            (2, '2HGCM82633A654321', 25000, 28, 20000, 'DEF456', '2019', 'Accord', 'Honda', 'Black', 'Sedan', 1)
        ]
        
        # Setup the mock cursor to return the mocked data
        self.mock_cursor.fetchall.return_value = mock_data

        # Call the function under test
        inventory = dbu.get_active_inventory()

        # Assert that the results match our expectations
        expected_inventory = [
            (1, '1HGCM82633A123456', 30000, 30, 25000, 'ABC123', '2020', 'Civic', 'Honda', 'Blue', 'Sedan', 1),
            (2, '2HGCM82633A654321', 25000, 28, 20000, 'DEF456', '2019', 'Accord', 'Honda', 'Black', 'Sedan', 1)
        ]
        self.assertEqual(inventory, expected_inventory)

        # Assert that the cursor executed the correct SQL query
        self.mock_cursor.execute.assert_called_once_with("select * from Vehicles where IsActive = 1")
        
    def test_valid_date_range(self):
        """Test with valid start and end dates."""
        start_date = '2024-01-01'
        end_date = '2024-01-10'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, 9)  # Expecting 9 days

    def test_end_date_before_start_date(self):
        """Test where the end date is before the start date."""
        start_date = '2024-01-10'
        end_date = '2024-01-01'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, -1)  # Expecting -1 for invalid range

    def test_invalid_date_format(self):
        """Test with invalid date format."""
        start_date = '2024/01/01'  # Invalid format
        end_date = '2024-01-10'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, -1)  # Expecting -1 for invalid format

    def test_non_date_string(self):
        """Test with non-date strings."""
        start_date = 'Hello'
        end_date = 'World'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, -1)  # Expecting -1 for invalid format

    def test_same_date(self):
        """Test when both dates are the same."""
        start_date = '2024-01-01'
        end_date = '2024-01-01'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, 0)  # Expecting 0 days
    
    def test_confirm_reservation_success(self):
        """Test confirming a reservation successfully."""
        reservation_id = 1
        
        # Mock cursor to return a not canceled reservation
        self.mock_cursor.fetchone.return_value = (0,)  # Not canceled
        dbu.confirm_reservation(reservation_id)
        
        # Check that the SELECT statement was executed
        self.mock_cursor.execute.assert_any_call(
            "SELECT Canceled FROM Reservations WHERE ReservationId = %s", 
            (reservation_id,)
        )
        
        # Check that the update statement was executed
        self.mock_cursor.execute.assert_any_call(
            "UPDATE Reservations SET Confirmed = 1 WHERE ReservationId = %s", 
            (reservation_id,)
        )
        
        # Check that the commit was called
        self.mock_db.commit.assert_called_once()
        
    def test_confirm_reservation_canceled(self):
        """Test confirming a reservation that is already canceled."""
        reservation_id = 2
        
        # Mock cursor to return a canceled reservation
        self.mock_cursor.fetchone.return_value = (1,)  # Canceled
        dbu.confirm_reservation(reservation_id)

        # Ensure the SELECT statement was executed
        self.mock_cursor.execute.assert_any_call(
            "SELECT Canceled FROM Reservations WHERE ReservationId = %s", 
            (reservation_id,)
        )
        
        # Ensure the update statement was NOT executed
        self.assertNotIn(
            "UPDATE Reservations SET Confirmed = 1 WHERE ReservationId = %s", 
            [call[0][0] for call in self.mock_cursor.execute.call_args_list]
        )
        
        # Check that commit was not called
        self.mock_db.commit.assert_not_called()

    def test_confirm_reservation_not_found(self):
        """Test confirming a reservation that does not exist."""
        reservation_id = 3
        
        # Mock cursor to return None (reservation not found)
        self.mock_cursor.fetchone.return_value = None
        dbu.confirm_reservation(reservation_id)

        # Ensure the SELECT statement was executed
        self.mock_cursor.execute.assert_any_call(
            "SELECT Canceled FROM Reservations WHERE ReservationId = %s", 
            (reservation_id,)
        )
        
        # Ensure the update statement was NOT executed
        self.assertNotIn(
            "UPDATE Reservations SET Confirmed = 1 WHERE ReservationId = %s", 
            [call[0][0] for call in self.mock_cursor.execute.call_args_list]
        )
        
        # Check that commit was not called
        self.mock_db.commit.assert_not_called()

if __name__ == "__main__":
    unittest.main()
