from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
# from .models import Entry

# Create your views here.
def hello_map(request):
    return render(request, "locations/hello_map.html", context={}) 

# class EntryListViews(ListView):
#    queryset = Entry.objects.filter(point__isnull=False)
