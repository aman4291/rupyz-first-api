from django.urls import path

from staff_api.views import ListStaffData, CreateStaffData, UpdateStaffData, DeleteStaffData


urlpatterns = [
    path('staff/', ListStaffData.as_view()),
    path('create/', CreateStaffData.as_view()),
    path('update/', UpdateStaffData.as_view()),
    path('delete/', DeleteStaffData.as_view()),
]
