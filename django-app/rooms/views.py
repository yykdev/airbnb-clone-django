from django.http import Http404
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from db.models import Room


class HomeView(ListView):

    model = Room
    template_name = "rooms/room_list.html"
    paginate_by = 10
    # paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        now = timezone.now()

        context["now"] = now

        return context


def room_detail(request, id):

    try:

        room = Room.objects.get(id=id)

        context = {
            'room': room,
        }

        return render(request, 'rooms/detail.html', context=context)

    except Room.DoesNotExist:

        raise Http404()
