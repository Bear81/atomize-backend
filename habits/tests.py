from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Habit, LogEntry
from django.utils.timezone import now

# Create your tests here.

class HabitLogTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass1234')
        self.client.login(username='tester', password='pass1234')

        self.habit = Habit.objects.create(
            owner=self.user,
            title='Test Habit',
            description='This is a test habit',
            goal_type='daily'
        )

        self.log = LogEntry.objects.create(
            owner=self.user,
            habit=self.habit,
            status='done',
            note='Test note'
        )

    def test_create_habit(self):
        response = self.client.post('/habits/', {
            'title': 'New Habit',
            'description': 'Desc',
            'goal_type': 'weekly',
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_habits(self):
        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habit(self):
        response = self.client.get(f'/habits/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        response = self.client.patch(f'/habits/{self.habit.id}/', {
            'description': 'Updated'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        response = self.client.delete(f'/habits/{self.habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_log(self):
        response = self.client.post('/habits/logs/', {
            'habit': self.habit.id,
            'status': 'partial',
            'note': 'Created via test'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_logs(self):
        response = self.client.get('/habits/logs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_logs_by_habit(self):
        response = self.client.get(f'/habits/logs/?habit={self.habit.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_logs_by_date(self):
        date_str = self.log.timestamp.date().isoformat()
        response = self.client.get(f'/habits/logs/?date={date_str}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_log(self):
        response = self.client.get(f'/habits/logs/{self.log.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_log(self):
        response = self.client.patch(f'/habits/logs/{self.log.id}/', {
            'note': 'Updated note'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_log(self):
        response = self.client.delete(f'/habits/logs/{self.log.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)