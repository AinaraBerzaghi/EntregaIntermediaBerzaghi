from django import forms


class formulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
