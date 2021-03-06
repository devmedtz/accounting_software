from django.urls import path, include
from django.contrib.auth import views as auth_views

from .import views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('confirm-email/<str:user_id>/<str:token>/',
         views.ConfirmRegistrationView.as_view(), name='confirm-email'),
    path('<slug:slug>/profile/', views.UserProfileView.as_view(),
         name='user-profile'),
    path('<slug:slug>/profile/update/', views.UserProfileUpdateView.as_view(),
         name='user-profile'),
    path('', include('django.contrib.auth.urls')),
]