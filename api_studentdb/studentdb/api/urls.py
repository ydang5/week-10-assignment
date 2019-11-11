from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('studentdb',views.StudentDbDetail.as_view()),
    path('studentdetail/<student_number>',views.GetStudentAPIView.as_view()),
    path('studentupdate/<student_number>/<age>',views.UpdateStudentAPIView.as_view()),
    path('studentdelete',views.ClearStudentAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
