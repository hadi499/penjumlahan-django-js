from django.shortcuts import render, redirect

from blog.forms import GajiForm
from .models import Gaji


def home(request):
    gaji = Gaji.objects.all()

    context = {
        'gaji': gaji,
    }

    return render(request, 'index.html', context)


def create(request):
    form = GajiForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('home')

    return render(request, 'create.html')
