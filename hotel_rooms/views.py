from django.shortcuts import render

# Create your views here.

def rooms(request):
    return render(request, 'hotel_rooms/rooms.html')
