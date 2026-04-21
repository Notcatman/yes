from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('vacancies/post/', views.post_vacancy, name='post_vacancy'),
    path('vacancies/<int:vacancy_id>/apply/', views.apply_vacancy, name='apply_vacancy'),
    path('vacancies/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
]