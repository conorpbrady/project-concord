from django.urls import path
from v1 import views

urlpatterns = [
        path('v1/weight', views.WeightList.as_view())
        ]
