from django.views import generic

from blog.models import Post
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

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
    
