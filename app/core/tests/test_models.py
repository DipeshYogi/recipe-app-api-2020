from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is succesful"""
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test if email for new user is normalized"""
        email = 'testemail@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test12311')
        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Test creating user with no email address"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'Test12323')

    def test_create_new_superuser(self):
        """test creating a new super user"""
        user = get_user_model().objects.create_superuser(
                'test@gmail.com',
                'test123')

        self.assertTrue(user.is_superuser) #is_superuser is included as part of PermissionsMixin
        self.assertTrue(user.is_staff)
