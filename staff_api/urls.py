from django.urls import path

from staff_api.views import StaffData


urlpatterns = [
    path('staff/', StaffData.as_view()),
]
