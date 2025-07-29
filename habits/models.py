from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    GOAL_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    owner = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='habits'
)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    goal_type = models.CharField(max_length=20, choices=GOAL_CHOICES, default='daily')
    frequency = models.CharField(max_length=50, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class LogEntry(models.Model):
    STATUS_CHOICES = [
        ('done', 'Done'),
        ('skipped', 'Skipped'),
        ('partial', 'Partial'),
    ]

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')
    owner = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='habit_log_entries'
)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='done')

    def __str__(self):
        return f"{self.habit.title} - {self.status} ({self.timestamp.date()})"
