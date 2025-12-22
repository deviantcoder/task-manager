from django.urls import path
from allauth.account import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='account_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='account_logout'),
    path('accounts/signup/', auth_views.SignupView.as_view(), name='account_signup'),
]
