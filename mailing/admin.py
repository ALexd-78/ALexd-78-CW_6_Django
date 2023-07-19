from django.contrib import admin

from mailing.models import Client, Message, SetMessage, LogMessage

# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Blog)
# admin.site.register(Version)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active')
    search_fields = ('last_name',)
    list_filter = ('first_name', 'last_name', 'is_active')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name', 'is_publication')

@admin.register(SetMessage)
class SetMessageAdmin(admin.ModelAdmin):
    # list_display = ('message', 'mailing_time', 'frequency', 'status')
    list_display = ('message', 'mailing_time',)
    # search_fields = ('frequency', 'status')
    search_fields = ('mailing_time',)
    list_filter = ('mailing_time', 'frequency', 'status')
    list_filter = ('mailing_time',)
@admin.register(LogMessage)
class LogMessageAdmin(admin.ModelAdmin):
    # list_display = ('product', 'name', 'number', 'is_active')
    list_display = ('message', 'last_try', 'status_try')
    # search_fields = ('status_try', 'server_response')
    search_fields = ('status_try',)
    # list_filter = ('last_try', 'status_try', 'server_response')
    list_filter = ('last_try', 'status_try',)


