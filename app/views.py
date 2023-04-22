from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',d)

def display_access(request):
    LOW=AccessRecord.objects.all()
    d={'access':LOW}
    return render(request,'display_access.html',d)
