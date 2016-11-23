from django.contrib import admin
from .models import Safra
from servicos.models import Servico



class SafraAdmin(admin.ModelAdmin):
    actions = ['atualizar_servicos']

    def atualizar_servicos(self, request, queryset):
        for safra in queryset:
            safra.atualizar_servicos()
        self.message_user(request, "Preços dos serviços atualizados com sucesso")

admin.site.register(Safra, SafraAdmin)