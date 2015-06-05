from django.shortcuts import render, redirect
# from django.template import*
from .models import Movie
from .models import Projection


def home(request):
    movies = Movie.objects.all().order_by('id')
    projections = Projection.objects.all()
    return render(request, "home.html", locals())


def showReservationForm(request, projection_id):
    try:
        projection_id = int(projection_id)
    except:
        return redirect('/')

    if projection_id < 1:
        return redirect('/')

    projection = Projection.objects.get(id=projection_id)
    return render(request, "reservation.html", locals())
