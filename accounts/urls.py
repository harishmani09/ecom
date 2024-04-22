from django.urls import path
from .views import (
    register,
    login,
    logout,
    activate,
    dashboard,
    forgot_password,
    resetpassword_validate,
    reset_password,
)

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("forgot_password/", forgot_password, name="forgot_password"),
    path(
        "resetpassword_validate/<uidb64>/<token>/",
        resetpassword_validate,
        name="resetpassword_validate",
    ),
    path("reset_password/", reset_password, name="reset_password"),
]
