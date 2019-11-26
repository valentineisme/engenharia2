from django.contrib import admin
from .models import usuario, marca_carro, modelo_carro, veiculos, leilao

admin.site.register(usuario)
admin.site.register(marca_carro)
admin.site.register(modelo_carro)
admin.site.register(veiculos)
admin.site.register(leilao)

# Register your models here.
