from django.shortcuts import render
from chartapp.models import show
# Create your views here.
def home(request):
    zoneH=show.objects.all().count()
    context= {
        "zoneH": zoneH,
    }
    return render(request, 'core/index.html', context)