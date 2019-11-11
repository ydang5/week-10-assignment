from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api', views.GetVersion.as_view()),
    path('api/add',views.AddNumber.as_view()),
    path('api/result',views.ResultAPIView.as_view()),
    path('api/clear',views.ClearResult.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
