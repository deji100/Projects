from django.
from .models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(help_text='Please enter the category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
        
    class Meta:
        model = Category
        fields = ('name',)