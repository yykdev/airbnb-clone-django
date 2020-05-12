from math import ceil

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView

from db.models import Room


class HomeView(ListView):

    model = Room
    template_name = "rooms/room_list.html"
    paginate_by = 10
    # paginate_orphans = 5
    ordering = "created"
