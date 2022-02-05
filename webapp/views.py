from django.shortcuts import render
from django.views import generic
from v1.models import Weight, Exercise, Lift
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'some_name'

    def queryset(self):
        return Weight.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['weight_listing'] = self.queryset()
        # context['lift_listing'] = Lift.objects.all()
        return context

class WeightView(generic.ListView):
    template_name = 'weight.html'
    context_object_name = 'weight'

    def queryset(self):
        return Weight.objects.all()

class ExerciseView(generic.ListView):
    template_name = 'exercise.html'
    context_object_name = 'exercise'

    def queryset(self):
        return Exercise.objects.all()

class LiftsView(generic.ListView):
    template_name = 'lifts.html'
    context_object_name = 'lifts'

    def queryset(self):
        return Lift.objects.all()

