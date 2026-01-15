from django.db import models
from account.models import User, GymBranch

class WorkoutPlan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    gym_branch = models.ForeignKey(GymBranch, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class WorkoutTask(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('in_progress','In Progress'),
        ('completed','Completed'),
    ]

    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.workout_plan.title} -> {self.member.name}"
