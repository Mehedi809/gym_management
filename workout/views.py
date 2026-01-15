from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import WorkoutPlan, WorkoutTask
from .serializers import WorkoutPlanSerializer, WorkoutTaskSerializer

# PLAN
class WorkoutPlanListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return WorkoutPlan.objects.all()
        return WorkoutPlan.objects.filter(gym_branch=user.gym_branch)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, gym_branch=self.request.user.gym_branch)


class WorkoutPlanRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return WorkoutPlan.objects.all()
        return WorkoutPlan.objects.filter(gym_branch=user.gym_branch)


# TASK
class WorkoutTaskListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutTaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return WorkoutTask.objects.all()
        if user.role == 'MEMBER':
            return WorkoutTask.objects.filter(member=user)
        return WorkoutTask.objects.filter(workout_plan__gym_branch=user.gym_branch)


class WorkoutTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutTaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return WorkoutTask.objects.all()
        if user.role == 'MEMBER':
            return WorkoutTask.objects.filter(member=user)
        return WorkoutTask.objects.filter(workout_plan__gym_branch=user.gym_branch)
