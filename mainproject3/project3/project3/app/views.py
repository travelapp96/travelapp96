from django.shortcuts import render
from .models import Place, Team


def home(request):
    obj = Place.objects.all()  # fetching all objects of place
    obj_2 = Team.objects.all()
    return render(request, "index.html", {'result': obj ,'meet':obj_2},)
