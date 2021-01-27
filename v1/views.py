from v1.models import Weight
from v1.serializers import WeightSerializer
from rest_framework import generics

# Create your views here.

class Weight(generics.ListAPIView):
   queryset = Weight.objects.all()
   serializer_class = WeightSerializer
