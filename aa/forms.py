from django import forms
from .models import usuario

class UsuarioForm(forms.ModelForm):

    nome = forms.CharField(max_length=78, help_text='Nome', widget=forms.TextInput(attrs={"required": True}))
    # sobrenome = forms.CharField(max_length=128, help_text='Sobrenome', widget=forms.TextInput(attrs={"required": True}))
    cpf = forms.CharField(max_length=128, help_text='CPF', widget=forms.TextInput(attrs={"name": "cpf"}))
    telefone = forms.CharField(max_length=15, help_text='Telefone', widget=forms.TextInput(attrs={"name": "telefone"}))
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'name': 'data_nascimento', 'required': True}))
    email = forms.CharField(max_length=128, help_text='E-mail', widget=forms.TextInput(attrs={"required": True}))
    senha = forms.CharField(max_length=128, help_text='Senha', widget=forms.PasswordInput(attrs={'required': True}))

    class Meta:
        model = usuario
        fields = ('nome','cpf','telefone','data_nascimento','email','senha')