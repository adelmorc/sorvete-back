from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.FornecedorCreateListView.as_view()),
    path('<int:pk>/', views.FornecedorRetrieveUpdateDestroyView.as_view()),
]
