from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }