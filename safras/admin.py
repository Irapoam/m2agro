from django.contrib import admin
from .models import Safra
from servicos.models import Servico



class SafraAdmin(admin.ModelAdmin):
    actions = ['atualizar_servicos']


    def atualizar_servicos(self, request, queryset):
    
        for safra in queryset:
            servicos = Servico.objects.filter(safra=safra)
            for servico in servicos:
                total = 0
                for servico_produto in servico.servico_produto.all():
                    total += servico_produto.quantidade * servico_produto.produto.preco
                servico.custo_total = total
                servico.save()

        self.message_user(request, "Preços dos serviços atualizados com sucesso")



admin.site.register(Safra, SafraAdmin)


