from  django import forms

from mailing.models import Client, Message, SetMessage, LogMessage


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        # fields = ('name', 'description', 'category', 'unit_price',)
        # exclude = ('is_publicate',)


class MessageForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'
        # fields = ('name', 'description', 'category', 'unit_price',)
        # exclude = ('is_publication',)


class SetMessageForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = SetMessage
        fields = '__all__'


class LogMessageForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = LogMessage
        fields = '__all__'


class UserForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'
        # fields = ('name', 'description', 'category', 'unit_price',)
        # exclude = ('is_publicate',)