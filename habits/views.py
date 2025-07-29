from rest_framework import generics, permissions
from .models import Habit
from .serializers import HabitSerializer, LogEntrySerializer
from .models import LogEntry


class HabitList(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HabitDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class LogEntryList(generics.ListCreateAPIView):
    serializer_class = LogEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LogEntry.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LogEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LogEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LogEntry.objects.filter(owner=self.request.user)