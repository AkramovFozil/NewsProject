from django.urls import path
from .views import dashboard, user_register, user_edit
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/', dashboard, name='user-profile'),
    path('user_edit/', user_edit, name='user_edit'),
    path('signup/', user_register, name='user-register'),
]
