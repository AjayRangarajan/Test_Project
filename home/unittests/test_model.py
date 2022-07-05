from django.test import TestCase
from django.contrib.auth.models import User
import os
class UserTestCase(TestCase):
	def setUp(self):
		User.objects.create_user(username="test_user", password="test_user_password")

	def test_user_created(self):
		print(os.environ.get('MSG'))
		test_user = User.objects.get(username="test_user")
		self.assertEqual(test_user.username, 'test_user')

	def test_environment_variable(self):
		self.assertEqual(os.environ.get('MSG'), "==================HELLO==================")