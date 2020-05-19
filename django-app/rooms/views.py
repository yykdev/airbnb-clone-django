from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from django.core.paginator import Paginator

from db.models import Room
from rooms.forms import SearchForm


class HomeView(ListView):

    model = Room
    template_name = "rooms/room_list.html"
    paginate_by = 8
    # paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    model = Room
    template_name = "rooms/room_detail.html"
    # pk_url_kwarg = "id" # default 'pk'


class Search(View):
    def get(self, request):

        country = request.GET.get("country")

        if country:
            form = SearchForm(request.GET)

            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                is_superhost = form.cleaned_data.get("is_superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Aniwhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if is_superhost is True:
                    filter_args["host__is_superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = Room.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                context = {
                    "form": form,
                    "rooms": rooms,
                    "query_string": request.environ.get("QUERY_STRING"),
                }

                return render(request, "rooms/room_search.html", context=context)

        else:
            form = SearchForm()

        return render(request, "rooms/room_search.html", context={"form": form})
