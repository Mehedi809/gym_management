from rest_framework import serializers
from .models import User, GymBranch

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'name', 'role', 'gym_branch', 'password']
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'name', 'role', 'gym_branch', 'password']
        read_only_fields = ['id']

    def validate(self, data):
        request_user = self.context['request'].user
        
        if request_user.role == 'MANAGER':
            if data.get('role') not in ['TRAINER', 'MEMBER']:
                raise serializers.ValidationError("Managers can only create Trainers or Members.")
            data['gym_branch'] = request_user.gym_branch

        if data.get('role') == 'TRAINER':
            branch = data.get('gym_branch')
            if User.objects.filter(gym_branch=branch, role='TRAINER').count() >= 3:
                raise serializers.ValidationError("This branch already has 3 trainers.")
        
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    def validate(self, data):
        if data.get('role') == 'TRAINER' and data.get('gym_branch'):
            count = User.objects.filter(gym_branch=data['gym_branch'], role='TRAINER').count()
            if count >= 3:
                raise serializers.ValidationError("Maximum 3 trainers allowed per branch.")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)