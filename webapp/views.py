from django.shortcuts import render
from django.views import generic
from v1.models import Weight, Exercise, Lift
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexView(generic.base.TemplateView):
    template_name = 'index.html'

class WeightView(LoginRequiredMixin, generic.ListView):
    template_name = 'weight.html'
    context_object_name = 'weight'

    def queryset(self):
        return Weight.objects.filter(owner=self.request.user)

class ExerciseView(LoginRequiredMixin, generic.ListView):
    template_name = 'exercise.html'
    context_object_name = 'exercise'

    def queryset(self):
        return Exercise.objects.filter(owner=self.request.user)

class LiftsView(LoginRequiredMixin, generic.ListView):
    template_name = 'lifts.html'
    context_object_name = 'lifts'

    def queryset(self):
        return Lift.objects.filter(owner=self.request.user)

