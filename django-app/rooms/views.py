from math import ceil

from django.shortcuts import render

from db.models import Room


def all_rooms(request):

    page = request.GET.get('page', 1)

    try:
        page = int(page or 1)
    except ValueError:
        page = 1
    page_size = 5
    limit = page * page_size
    offset = limit - page_size

    rooms = Room.objects.all()[offset:limit]
    page_count = ceil(Room.objects.count() / page_size)

    context = {
        'rooms': rooms,
        'page': page,
        'page_count': page_count,
        'page_range': range(1, page_count + 1),
    }

    return render(request, 'rooms/home.html', context=context)
