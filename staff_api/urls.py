from django.urls import path

from staff_api.views import DetailAndUpdateAPIView, ListAndCreateStaffAPIView, DeleteStaffAPIView

urlpatterns = [
    path('', ListAndCreateStaffAPIView.as_view()),
    path('<int:pk>/', DetailAndUpdateAPIView.as_view()),
    path('<int:pk>/delete/', DeleteStaffAPIView.as_view()),
]
