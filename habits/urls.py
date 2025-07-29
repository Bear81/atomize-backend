from django.urls import path
from .views import (
    HabitList, HabitDetail,
    LogEntryList, LogEntryDetail,
)

urlpatterns = [
    # Habit endpoints
    path('habits/', HabitList.as_view()),
    path('habits/<int:pk>/', HabitDetail.as_view()),
    # LogEntry endpoints
    path('habits/logs/', LogEntryList.as_view()),
    path('habits/logs/<int:pk>/', LogEntryDetail.as_view()),
]
