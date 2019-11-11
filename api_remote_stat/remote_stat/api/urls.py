from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/add',views.InputDataAPIView.as_view()),
    path('api/average',views.AverageAPIView.as_view()),
    path('api/mean',views.MeanAPIView.as_view()),
    path('api/stat',views.StatAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
