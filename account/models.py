from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import UserManager

class GymBranch(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('TRAINER', 'Trainer'),
        ('MEMBER', 'Member'),
    ]
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    gym_branch = models.ForeignKey(GymBranch, on_delete=models.SET_NULL, null=True, blank=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # Clash fix
    groups = models.ManyToManyField('auth.Group', related_name='gym_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='gym_user_permissions', blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'role']