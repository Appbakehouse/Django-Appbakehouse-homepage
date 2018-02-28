from django.views import generic

from blog.models import Post
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

#--- ListView
class PostListView(generic.ListView) :
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostTagTemplateView(TaggedObjectList) :
    model = Post
    template_name = 'tagging/tagging_post_list.html'

#--- DetailView
class PostDetailView(generic.DetailView) :
    model = Post

#--- ArchiveView
class PostArchiveIndexView(generic.ArchiveIndexView) :
    model = Post
    date_field = 'modify_date'

class PostYearArchiveView(generic.YearArchiveView) :
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMonthArchiveView(generic.MonthArchiveView) :
    model = Post
    date_field = 'modify_date'

class PostDayArchiveView(generic.DayArchiveView) :
    model = Post
    date_field = 'modify_date'

class PostTodayArchiveView(generic.TodayArchiveView) :
    model = Post
    date_field = 'modify_date'

#--- TemplateView
class TagTemplateView(generic.TemplateView) :
    template_name = 'tagging/tagging_cloud.html'
    
#--- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)