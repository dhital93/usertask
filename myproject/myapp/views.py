from django.shortcuts import render, get_object_or_404, render
from .models import Main

# Create your views here.


def home(request):
    site = Main.objects.all()
    if request.method == 'POST':
        text = request.POST.get('input')
        if text == '':
            print('error')
        b = Main(taxk=text)
        b.save()

    return render(request, 'index.html', {'site': site})
