from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = "test@example.com"
        password = "test12356"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@EXAMPLE.COM"
        user = get_user_model().objects.create_user(email, "test12356")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a user without an email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test12356")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "super@example.com",
            "superpass123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_first_and_last_name_are_optional(self):
        """Test first_name and last_name are optional"""
        user = get_user_model().objects.create_user(
            email="user@example.com",
            password="test12356",
        )

        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str_returns_email(self):
        """Test the string representation is the email"""
        user = get_user_model().objects.create_user(
            email="user@example.com",
            password="testpass123",
        )

        self.assertEqual(str(user), user.email)
