from v1.models import Weight, Exercise, Lift
from v1.serializers import WeightSerializer, ExerciseSerializer, LiftSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
# Create your views here.

class WeightList(generics.ListCreateAPIView):

    def get_queryset(self):
        return Weight.objects.all().filter(owner = self.request.user)
        
   #queryset = Weight.objects.filter(owner = request.user)
    serializer_class = WeightSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user, record_date = timezone.now())


class ExerciseList(generics.ListCreateAPIView):

    def get_queryset(self):
        return Exercise.objects.all().filter(owner = self.request.user)

    serializer_class = ExerciseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user, record_date = timezone.now())

class LiftList(generics.ListCreateAPIView):

    def get_queryset(self):
        return Lift.objects.all().filter(owner = self.request.user)

    serializer_class = LiftSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user, record_date = timezone.now())
        
