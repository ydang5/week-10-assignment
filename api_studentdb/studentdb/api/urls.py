from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('studentdb',views.StudentDbDetail.as_view()),
    path('add',views.AddStudentAPIView.as_view()),
    path('studentdetail/<student_number>',views.GetStudentAPIView.as_view()),
    path('studentupdate/<student_number>',views.UpdateStudentAPIView.as_view()),
    path('studentdelete/<student_number>',views.ClearStudentAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
