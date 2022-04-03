from django.urls import path
from .views import (loginuser, notification,
otherprofile, logoutuser, registration,
 change_password, activate, userprofile,
ownerprofile, tuitionprofile)
from django.contrib.auth.views import (PasswordResetView,
 PasswordResetDoneView, PasswordResetConfirmView,
  PasswordResetCompleteView)


urlpatterns = [
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('signup/', registration, name='signup'),
    path('notification/', notification, name='notification'),
    path('change_pass/', change_password, name='change_pass'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('userprofile/', userprofile, name='userprofile'),
    path('otherprofile/<str:username>/', otherprofile, name='otherprofile'),
    path('ownerprofile/', ownerprofile, name='ownerprofile'),
    path('tuitionprofile/', tuitionprofile, name='tuitionprofile'),

    #password reset url
    path('reset/password/', PasswordResetView.as_view(template_name='session/reset_pass.html'), name='password_reset'),
    path('reset/password/done/', PasswordResetDoneView.as_view(template_name='session/reset_pass_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='session/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='session/password_reset_complete.html'), name='password_reset_complete'),

]
