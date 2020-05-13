from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries

from db.models import Room, RoomType, Amenity, Facility


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

    city = str.capitalize(request.GET.get("city", "Anywhere"))
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", "0"))

    price = request.GET.get('price', 0)
    guests = request.GET.get('guests', 0)
    bedrooms = request.GET.get('bedrooms', 0)
    beds = request.GET.get('beds', 0)
    baths = request.GET.get('baths', 0)
    instant = request.GET.get('instant', False)
    super_host = request.GET.get('super_host', False)
    s_amenities = request.GET.getlist('amenities', 0)
    s_facilities = request.GET.getlist('facilities', 0)

    form = {
        'city': city,
        's_country': country,
        's_room_type': room_type,
        'price': price,
        'guests': guests,
        'bedrooms': bedrooms,
        'beds': beds,
        'baths': baths,
        'instant': instant,
        'super_host': super_host,
    }

    room_types = RoomType.objects.all()
    amentities = Amenity.objects.all()
    facilities = Facility.objects.all()

    choices = {
        "countries": countries,
        'room_types': room_types,
        'amenities': amentities,
        'facilities': facilities,
        's_amenities': s_amenities,
        's_facilities': s_facilities,
    }

    context = {
        **form,
        **choices,
    }

    return render(request, 'rooms/room_search.html', context=context)
