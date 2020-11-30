from django import forms
from .models import Post,Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':7}))
    class Meta:
        model = Post
        fields = ['content', 'image']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

