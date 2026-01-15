from django.urls import path
from .views import LoginView, UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserRetrieveUpdateDestroyView.as_view(), name='user-rud'),
]
