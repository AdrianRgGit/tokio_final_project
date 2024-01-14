from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "genre", "director", "duration", "image", "description", "release_date"]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Género'}),
            'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Director'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': 'Título', 'genre': 'Género', 'director': 'Director', 'duration': 'Duración', 'image': 'Imágen',
            'description': 'Descripción', 'release_date': 'Fecha de estreno'
        }
