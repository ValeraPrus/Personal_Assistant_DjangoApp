from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.main, name='main'),
    path('contacts/', views.contact_book, name='contact_book'),
    path('search/', views.search_contacts, name='search_contacts'),
    path('add/', views.add_contact, name='add_contact'),
    path('birthdays/', views.birthday_list, name='birthday_list'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]
