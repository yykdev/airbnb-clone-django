from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries

from db.models import Room, RoomType


class HomeView(ListView):

    model = Room
    template_name = "rooms/room_list.html"
    paginate_by = 10
    # paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    model = Room
    template_name = "rooms/room_detail.html"
    # pk_url_kwarg = "id" # default 'pk'


def search(request):

    city = request.GET.get("city", "anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", "0"))
    room_types = RoomType.objects.all()

    form = {
        'city': city,
        's_country': country,
        's_room_type': room_type,
    }

    choices = {
        "countries": countries,
        'room_types': room_types,
    }

    context = {
        **form,
        **choices,
    }

    return render(request, 'rooms/room_search.html', context=context)
