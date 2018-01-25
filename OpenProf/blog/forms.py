from django import forms

from .models import Comment,Annonce,Prof


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ['auteur', 'email', 'contenu','articleRef',]

class ProfForm(forms.ModelForm):

    class Meta:

        model = Prof
        exclude = ['slug',]

class AnnonceForm(forms.ModelForm):

    class Meta:

        model = Annonce
        exclude = ['slug','date',]