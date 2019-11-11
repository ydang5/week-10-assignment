from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('login',views.AccountLoginAPI.as_view()),
    path('register',views.AccountRegisterAPI.as_view()),
    path('detail',views.AccountDetailAPI.as_view()),
    path('changepassword',views.ChangePasswordAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
