from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import SignUpView, DashboardView, ActivateAccountView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", auth_views.LoginView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path("activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
]