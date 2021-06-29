from django.urls import path

from api import views

urlpatterns = [
    path('course/create_course/', views.CreateCourseView.as_view()),
    path('course/delete_course_by_id/<int:pk>/', views.DeleteCourseByIdView.as_view()),
    path('course/delete_all_courses/', views.DeleteAllCoursesView.as_view()),
    path('course/update_course_by_id/<int:pk>/', views.UpdateCourseByIdView.as_view()),
    path('course/find_all_courses/', views.FindAllCoursesView.as_view()),
    path('course/find_course_by_id/<int:pk>/', views.FindCourseByIdView.as_view()),
]
