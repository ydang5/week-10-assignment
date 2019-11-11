from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('add',views.AddMember.as_view()),
    path('acceptance',views.AcceptanceAPI.as_view()),
    path('rejection',views.RejectionAPI.as_view()),
    path('airforce',views.AirforceAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
