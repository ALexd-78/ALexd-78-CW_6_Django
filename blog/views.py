from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog
from django.views import generic

class BlogListView(LoginRequiredMixin, generic.ListView):
    '''контроллер страницы статей'''
    model = Blog
    extra_context = {
        'title': 'Статьи'
    }

    # def get_queryset(self):
    #     '''фильтр на отображение'''
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_active=True)
    #     return queryset


class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    '''контроллер постраничного вывода информации о статье'''
    model = Blog

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['blog']
        return context_data

    def get_object(self, queryset=None):
        '''счётчик просмотров'''
        item = super().get_object(queryset)
        item.count_views += 1
        item.save()
        return item