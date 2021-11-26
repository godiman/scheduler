
from django.urls import path, re_path

from django.contrib.auth import views as auth_views

from scheduler.views import home_view

# app_name = AppName

urlpatterns = [
    path("", home_view, name="home"),
    
    # Custom password reset urls
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
]