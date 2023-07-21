from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Blog
from mailing.forms import ClientForm, MessageForm, UserForm
from mailing.models import Client, Message
from users.models import User


def index(request):
    '''контроллер главной страницы'''
    context = {
        'message_count': Message.objects.count(),
        # 'message_active_count': Message.objects.filter(status='START').count(),
        'unique_clients_count': Client.objects.values('email').distinct().count(),
        'blog_list': Blog.objects.order_by('?')[:3],
        'title': 'Главная'

    }
    return render(request, 'mailing/index.html', context)


class ClientListView(LoginRequiredMixin, generic.ListView):
    '''контроллер страницы клиентов'''
    model = Client
    extra_context = {
        'title': 'Клиенты'
    }

    def get_queryset(self):
        '''фильтр на отображение только клиентов пользователя'''
        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = Client.objects.all()
        else:
            queryset = Client.objects.filter(user=user)

        queryset = queryset.filter(is_active=True)
        return queryset


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    '''контроллер постраничного вывода информации о клиенте'''
    model = Client

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']

        return context_data


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    '''контроллер создания клиента'''
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        '''привязка создаваемого клиента к авторизованному пользователю'''
        client = form.save(commit=False)
        client.user = self.request.user
        client.save()
        return super(ClientCreateView, self).form_valid(form)


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    '''контроллер изменения клиента'''
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    '''контроллер удаления клиента'''
    model = Client
    success_url = reverse_lazy('mailing:client_list')
    # permission_required = 'mailing.delete_client'


class MessageListView(LoginRequiredMixin, generic.ListView):
    '''контроллер страницы рассылок'''
    model = Message
    extra_context = {
        'title': 'Рассылки'
    }

    def get_queryset(self):
        '''фильтр на отображение только клиентов пользователя'''
        # queryset = super().get_queryset()

        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = Message.objects.all()
        else:
            queryset = Message.objects.filter(user=user)

        queryset = queryset.filter(is_publication=True)
        return queryset


class MessageDetailView(LoginRequiredMixin, generic.DetailView):
    '''контроллер постраничного вывода информации о рассылках'''
    model = Message

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class MessageCreateView(LoginRequiredMixin, generic.CreateView):
    '''контроллер создания рассылки'''
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        '''привязка создаваемого рассылки к авторизованному пользователю'''
        form.instance.User = self.request.user
        return super(MessageCreateView, self).form_valid(form)


class MessageUpdateView(LoginRequiredMixin, generic.UpdateView):
    '''контроллер изменения рассылки'''
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, generic.DeleteView):
    '''контроллер удаления рассылки'''
    model = Message
    success_url = reverse_lazy('mailing:message_list')


def get_contacts(request):
    '''контроллер контактов'''
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'User {name} with phone {phone} send message: {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'mailing/contacts.html', context)


def get_messages(request):
    '''контроллер меню рассылки'''
    context = {
        'title': 'Меню рассылки'
    }
    return render(request, 'mailing/messages_menu.html', context)


class UserListView(LoginRequiredMixin, generic.ListView):
    '''Контроллер вывода пользователей'''
    model = User
    form_class = UserForm

    extra_context = {
        'title': 'Пользователи'
    }

    def get_queryset(self):
        '''фильтр на отображение только клиентов пользователя'''
        # queryset = super().get_queryset()

        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = User.objects.all()
        else:
            pass

        queryset = queryset.filter(is_publication=True)
        return queryset