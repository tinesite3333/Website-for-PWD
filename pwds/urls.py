# pwds/urls.py
from django.urls import path
from . import views

app_name = 'pwds'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('booking/<int:booking_id>/accept/', views.accept_booking, name='accept_booking'),
    path('booking/<int:booking_id>/decline/', views.reject_booking, name='decline_booking'),
]


