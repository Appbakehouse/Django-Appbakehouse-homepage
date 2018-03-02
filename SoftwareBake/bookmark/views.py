from django.shortcuts import render
from bookmark.models import Bookmark
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from SoftwareBake.view import LoginRequiredMixin


class IndexView(generic.ListView):
    model = Bookmark

class DetailView(generic.DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)

class BookmarkChangeListView(LoginRequiredMixin, generic.ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(LoginRequiredMixin, UpdateView) :
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(LoginRequiredMixin, DeleteView) :
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')