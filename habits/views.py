from rest_framework import generics, permissions
from rest_framework.request import Request
from django.utils.dateparse import parse_date
from .models import Habit, LogEntry
from .serializers import HabitSerializer, LogEntrySerializer
from rest_framework.request import Request
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# ---------------------------
# Habit Views
# ---------------------------

@method_decorator(csrf_exempt, name='dispatch')
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


# ---------------------------
# LogEntry Views
# ---------------------------

@method_decorator(csrf_exempt, name='dispatch')
class LogEntryList(generics.ListCreateAPIView):
    serializer_class = LogEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        request: Request = self.request
        queryset = LogEntry.objects.filter(owner=request.user)
        habit_id = request.query_params.get('habit')
        date_str = request.query_params.get('date')

        if habit_id:
            queryset = queryset.filter(habit__id=habit_id)
        if date_str:
            parsed_date = parse_date(date_str)
            if parsed_date:
                queryset = queryset.filter(timestamp__date=parsed_date)

        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LogEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LogEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LogEntry.objects.filter(owner=self.request.user)
