from django.shortcuts import render
from django.utils import timezone
from .models import EventModel
def timer(request):
    event = EventModel.objects.first()
    if event:
        time_remaining = event.event_date - timezone.now()
        hour = time_remaining.seconds // 3600
        minute = (time_remaining.seconds % 3600) // 60
        seconds = time_remaining.seconds % 60
        data = {
            'name' : event.name,
            'hours' : hour,
            'minutes' : minute,
            'seconds' : seconds
        }
    else:
        data = {
            'name' : "Not found",
            'hours' : 0,
            'minutes' : 0,
            'seconds' : 0
        }

    content = {
        'data' : data
    }

    return render(request,'app.html',content)
