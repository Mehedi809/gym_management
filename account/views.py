from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, GymBranch
from .serializers import UserSerializer

# LOGIN
class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'role': user.role
            })
        return Response({"error":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# LIST + CREATE
class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return User.objects.all()
        elif user.role == 'MANAGER':
            return User.objects.filter(gym_branch=user.gym_branch)
        return User.objects.filter(id=user.id)

    def perform_create(self, serializer):
        creator = self.request.user
        role = self.request.data.get('role')
        if creator.role == 'ADMIN':
            serializer.save()
        elif creator.role == 'MANAGER':
            if role not in ['TRAINER','MEMBER']:
                raise Response({"error":"Manager can create only Trainer or Member"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(role=role, gym_branch=creator.gym_branch)
        else:
            raise Response({"error":"You are not allowed to create users"}, status=status.HTTP_403_FORBIDDEN)


# RETRIEVE + UPDATE + DELETE
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return User.objects.all()
        elif user.role == 'MANAGER':
            return User.objects.filter(gym_branch=user.gym_branch)
        return User.objects.filter(id=user.id)
