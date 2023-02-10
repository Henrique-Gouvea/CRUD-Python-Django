from django.urls import path
from .views import userAPI

urlpatterns = [
    path('', userAPI),
    path('<int:id>', userAPI)
]