from django.db import models
from django.contrib.auth.models import User
# from aa import views


class usuario(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, editable=False, on_delete=models.CASCADE)
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=128, null=False)
    telefone = models.CharField(max_length=128, null=False)
    data_nascimento = models.DateField(blank=True)
    email = models.CharField(max_length=128)
    senha = models.CharField(max_length=128, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def save(self):
        if not self.id:
            c = usuario.objects.filter(email=self.email).count()
            c_test = usuario.objects.filter(cpf=self.cpf).count()
            # if c:
            #     raise Exception("Email Existente")
            # if c_test:
            #     raise Exception("CPF Existente")

            usr = User.objects.filter(username=self.email)
            if usr:
                u = usr[0]
            else:
                u = User.objects.create_user(self.email, self.email, self.senha)
            u.save()
            self.user = u
        else:
            self.user.username = self.email
            self.user.email = self.email
            self.user.set_password(self.senha)
            self.user.save()

        super(usuario, self).save()

    def __str__(self):
        return self.nome

class modelo_carro(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Modelo Carro'
        verbose_name_plural = 'Modelos Carros'

    def __str__(self):
        return self.nome

class marca_carro(models.Model):
    nome = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Marca Carro'
        verbose_name_plural = 'Marcas Carros'

    def __str__(self):
        return self.nome

class veiculos(models.Model):
    modelo = models.ForeignKey(modelo_carro, on_delete=models.CASCADE)
    marca = models.ForeignKey(marca_carro, on_delete=models.CASCADE)
    ano_veiculo = models.CharField(max_length=128)
    cor = models.CharField(max_length=128)
    combustivel = models.CharField(max_length=128)
    placa = models.CharField(max_length=128)
    valor = models.CharField(max_length=128)
    documentacao = models.CharField(max_length=128)
    ipva = models.CharField(max_length=128)
    img = models.ImageField(upload_to='static/media/', blank=True)
    observacao = models.CharField(max_length=1280)

    class Meta:
     verbose_name = 'Veiculo'
     verbose_name_plural = 'Veiculos'

    def __str__(self):
     return self.modelo