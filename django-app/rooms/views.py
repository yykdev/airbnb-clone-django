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

    city = str.capitalize(request.GET.get("city", ""))
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", "0"))

    price = int(request.GET.get('price', 0))
    guests = int(request.GET.get('guests', 0))
    bedrooms = int(request.GET.get('bedrooms', 0))
    beds = int(request.GET.get('beds', 0))
    baths = int(request.GET.get('baths', 0))
    instant = bool(request.GET.get('instant', False))
    is_superhost = bool(request.GET.get('is_superhost', False))
    s_amenities = request.GET.getlist('amenities')
    s_facilities = request.GET.getlist('facilities')

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
        'is_superhost': is_superhost,
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

    filter_args = {}

    if city:
        filter_args["city__startwith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if is_superhost is True:
        filter_args["host__is_superhost"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facilities__pk"] = int(s_facility)

    rooms = Room.objects.filter(**filter_args)

    context = {
        **form,
        **choices,
        'rooms': rooms,
    }

    return render(request, 'rooms/room_search.html', context=context)
