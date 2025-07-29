from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.ProdutoCreateListView.as_view()),
    path('<int:pk>/', views.ProdutoRetrieveUpdateDestroyView.as_view()),
]
