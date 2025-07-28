from django.urls import path
from .views import HabitList, HabitDetail

urlpatterns = [
    path('habits/', HabitList.as_view()),
    path('habits/<int:pk>/', HabitDetail.as_view()),
]
