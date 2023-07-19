from  django import forms

from blog.models import Blog
from mailing.forms import FormStyleMixin


class BlogForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ('name', 'description', 'category', 'unit_price',)
        # exclude = ('is_publicate',)