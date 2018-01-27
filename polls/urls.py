from django.urls import path
from django.conf import settings
from . import views
from django.views.static import serve

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='polls'),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results', views.ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote', views.vote, name="vote"),
]