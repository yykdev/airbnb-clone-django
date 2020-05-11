from math import ceil

from django.shortcuts import render
from django.core.paginator import Paginator

from db.models import Room


def all_rooms(request):

    page = request.GET.get('page', 1)
    room_list = Room.objects.all()

    paginator = Paginator(room_list, 10)

    # page, get_page 차이
    # - page 의 경우 에러를 핸들링 할 수 있고
    # - get_page 의 경우 라이브러리 내에서 except 처리가 돼 있다.
    # rooms = paginator.page(page)
    rooms = paginator.get_page(page)

    context = {
        'page': rooms,
    }

    return render(request, 'rooms/home.html', context=context)
