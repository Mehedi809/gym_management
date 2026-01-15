from django.urls import path
from .views import (
    WorkoutPlanListCreateView, WorkoutPlanRetrieveUpdateDestroyView,
    WorkoutTaskListCreateView, WorkoutTaskRetrieveUpdateDestroyView
)

urlpatterns = [
    # Plans
    path('plans/', WorkoutPlanListCreateView.as_view(), name='plan-list-create'),
    path('plans/<int:id>/', WorkoutPlanRetrieveUpdateDestroyView.as_view(), name='plan-rud'),

    # Tasks
    path('tasks/', WorkoutTaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:id>/', WorkoutTaskRetrieveUpdateDestroyView.as_view(), name='task-rud'),
]
