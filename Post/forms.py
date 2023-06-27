

from django import forms
from .models import Post,Comment

class ScamForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'image')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)





class LikeForm(forms.Form):
    value = forms.IntegerField(widget=forms.HiddenInput())
    post_id = forms.IntegerField(widget=forms.HiddenInput())
