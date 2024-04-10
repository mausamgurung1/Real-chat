from django.contrib.auth import views as auth_views
from django.urls import path

from app import views as chat_views

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),  # Updated URL pattern name
    path("auth/login/", auth_views.LoginView.as_view(template_name="loginPage.html"), name="login-user"),
    path("auth/logout/", auth_views.LogoutView.as_view(), name="logout-user")
]
