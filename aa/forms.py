from django import forms
from .models import usuario, veiculos

cores = [('Preto', 'Preto'), ('Branco', 'Branco'),]
combustivel = [('Gasolina', 'Gasolina'), ('Alcool', 'Alcool'),]
ipva = [('S', 'Sim'), ('N', 'Não'),]
doc = [('S', 'Sim'), ('N', 'Não'),]

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

class VeiculoForm(forms.ModelForm):
    # modelo = models.ForeignKey(modelo_carro, on_delete=models.CASCADE)
    # marca = models.ForeignKey(marca_carro, on_delete=models.CASCADE)
    ano_veiculo = forms.CharField(max_length=4, help_text='Ano do Veículo', widget=forms.TextInput(attrs={"name":"ano"}))
    cor = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(attrs={"name":"cor"}), choices=cores, )
    combustivel = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(attrs={"name":"combustivel"}), choices=combustivel,)
    placa = forms.CharField(max_length=10, help_text='Placa do Veículo', widget=forms.TextInput(attrs={"name": "placa"}))
    valor = forms.CharField(max_length=128, help_text='Valor do Veículo', widget=forms.TextInput(attrs={"name": "valor"}))
    documentacao = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(attrs={"name":"doc"}), choices=doc,)
    ipva = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(attrs={"name":"ipva"}), choices=ipva,)
    img = forms.ImageField(required=True, widget=forms.FileInput(attrs={"name": "imagem_veiculo"}))
    observacao = forms.CharField(max_length=128, help_text='Descrição do Veículo', widget=forms.Textarea(attrs={"name": "observacao"}))

    class Meta:
        model = veiculos
        fields = '__all__'
        exclude = ('modelo', 'marca')