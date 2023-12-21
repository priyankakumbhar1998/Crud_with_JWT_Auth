from django.urls import path
from .views import create_person, show_person, retrieve_person, update_person, delete_person

urlpatterns = [
    path ('create/', create_person),
    path('show/', show_person),
    path('retrieve/<int:pk>/', retrieve_person),
    path ('update/<int:pk>/', update_person),
    path('delete/<int:pk>/', delete_person),

]
