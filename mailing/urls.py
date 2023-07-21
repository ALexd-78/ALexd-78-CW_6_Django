from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import ClientListView, get_contacts, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, \
    get_messages, index

app_name = MailingConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('messages_menu', get_messages, name='messages_menu'),
    path('contacts/', get_contacts, name='contacts'),

    path('clients/', cache_page(60)(ClientListView.as_view()), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_item'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    path('messages', cache_page(60)(MessageListView.as_view()), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_item'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),


]
