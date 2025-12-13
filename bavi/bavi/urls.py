from django.urls import path
from Mathapp import views
urlpatterns = [
    path('', views.eff, name='eff'),
]
