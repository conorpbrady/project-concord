from django.urls import path
from webapp import views

urlpatterns = [
        path('webapp/', views.IndexView.as_view(), name='index'),
        path('webapp/weight/', views.WeightView.as_view(), name='weight'),
        path('webapp/exercise/', views.ExerciseView.as_view(), name='exercise'),
        path('webapp/lifts/', views.LiftsView.as_view(), name='lifts'),
        ]

