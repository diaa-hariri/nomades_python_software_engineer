import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from unittest.mock import MagicMock, patch
from routes.users.user_service import UserService

class TestUserService(unittest.TestCase):

    def setUp(self):
        # Create a UserService instance
        self.user_service = UserService()
        
        # Mock the UserRepository instance inside UserService
        self.user_service.repository = MagicMock()

    def test_get_all(self):
        # Arrange
        self.user_service.repository.get_all.return_value = [{"id": "1", "username": "testuser"}]
        
        # Act
        result = self.user_service.get_all()
        
        # Assert
        self.assertEqual(result, [{"id": "1", "username": "testuser"}])
        self.user_service.repository.get_all.assert_called_once()

    def test_create_user(self):
        # Arrange
        user_data = {"username": "newuser", "password": "password123"}
        self.user_service.repository.get_user_by_username.side_effect = Exception("User not found")
        self.user_service.repository.create_user.return_value = {"id": "1", "username": "newuser"}

        # Act
        result = self.user_service.create_user(user_data)
        
        # Assert
        self.assertIn("id", result)
        self.assertEqual(result["username"], "newuser")
        self.user_service.repository.get_user_by_username.assert_called_once_with("newuser")
        self.user_service.repository.create_user.assert_called_once()

    def test_create_user_existing_username(self):
        # Arrange
        user_data = {"username": "existinguser", "password": "password123"}
        self.user_service.repository.get_user_by_username.return_value = {"id": "1", "username": "existinguser"}

        # Act & Assert
        with self.assertRaises(Exception) as context:
            self.user_service.create_user(user_data)
        self.assertIn("User with username existinguser already exists", str(context.exception))
        self.user_service.repository.get_user_by_username.assert_called_once_with("existinguser")
        self.user_service.repository.create_user.assert_not_called()

    def test_get_one(self):
        # Arrange
        self.user_service.repository.get_one.return_value = {"id": "1", "username": "testuser"}
        
        # Act
        result = self.user_service.get_one("1")
        
        # Assert
        self.assertEqual(result, {"id": "1", "username": "testuser"})
        self.user_service.repository.get_one.assert_called_once_with("1")

    # def test_update_one(self):
    #     # Arrange
    #     user_id = "1"
    #     updated_data = {"password": "newpassword123"}
    #     self.user_service.repository.get_one.return_value = {"id": "1", "username": "testuser"}
    #     self.user_service.repository.update_user.return_value = {"id": "1", "username": "testuser", "password": "hashed_password", "salt": "salt"}
        
    #     # Act
    #     result = self.user_service.update_one(user_id, updated_data)
        
    #     # Assert
    #     self.assertIn("id", result)
    #     self.assertEqual(result["username"], "testuser")
    #     self.user_service.repository.update_user.assert_called_once_with(user_id, unittest.mock.ANY)

    def test_delete_user(self):
        # Arrange
        user_id = "1"
        
        # Act
        self.user_service.delete_user(user_id)
        
        # Assert
        self.user_service.repository.delete_user.assert_called_once_with(user_id)

    def test_get_user_by_firstname(self):
        # Arrange
        firstname = "John"
        self.user_service.repository.get_user_by_firstname.return_value = [{"id": "1", "username": "john_doe", "firstname": "John"}]
        
        # Act
        result = self.user_service.get_user_by_firstname(firstname)
        
        # Assert
        self.assertEqual(result, [{"id": "1", "username": "john_doe", "firstname": "John"}])
        self.user_service.repository.get_user_by_firstname.assert_called_once_with(firstname)

if __name__ == '__main__':
    unittest.main()