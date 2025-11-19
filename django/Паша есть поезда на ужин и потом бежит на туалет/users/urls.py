from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView,
    PasswordResetCompleteView, PasswordResetConfirmView,
    PasswordResetDoneView, PasswordResetView
)
from django.urls import reverse_lazy
from django.urls import path

from . import views

# app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html', next_page='/'),
        name='выход'
    ),
    path(
        'signup/',
        views.SignUp.as_view(),
        name='регистрация'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/вход.html'),
        name='вход'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='users/password_change_form.html',
        ),
        name='password_change_form'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html',
        ),
        name='password_reset_done'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='users/сброс_пароля.html',
            email_template_name='users/письмо_сброс_пароля.html',
            subject_template_name='users/тема_сброс_пароля.txt',
            success_url=reverse_lazy('password_reset_done')
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/сброс_пароля_подтверждение.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

]
