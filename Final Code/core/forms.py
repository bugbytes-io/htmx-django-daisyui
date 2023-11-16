from django import forms
from core.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('description', 'is_completed')