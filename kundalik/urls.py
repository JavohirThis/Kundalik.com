from django.urls import path
from .views import ListStudentApiView, DetailStudentApiView
urlpatterns = [
    path('', ListStudentApiView.as_view()),
    path('<int:student_id>/',DetailStudentApiView.as_view())
]
