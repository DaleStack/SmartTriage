from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view, dashboard_patient_list

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    #DASHBOARD
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/patient-list/', dashboard_patient_list, name='dashboard-patient-list'),
]
