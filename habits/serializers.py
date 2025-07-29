from rest_framework import serializers
from .models import Habit, LogEntry

class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Habit
        fields = [
            'id', 'owner', 'title', 'description',
            'goal_type', 'frequency', 'priority',
            'is_active', 'created_at',
        ]


class LogEntrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LogEntry
        fields = '__all__'