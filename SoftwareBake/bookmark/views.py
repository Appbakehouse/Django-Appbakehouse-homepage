from django.shortcuts import render
from bookmark.models import Bookmark
from django.views import generic


class IndexView(generic.ListView):
    model = Bookmark

class DetailView(generic.DetailView):
    model = Bookmark