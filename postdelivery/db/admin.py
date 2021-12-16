from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Contract, Recipient, AdressSender, AdressRecipient, Route

class AdressRecipientAdmin(ModelAdmin):

    list_display = [
        "city", "street", "house", "flat" 
    ]
    search_fields =('city',)
    list_filter = [
        "city",
        "street",
    ]

class AdressSenderAdmin(ModelAdmin):

    list_display = [
        "city", "street", "house", "flat" 
    ]
    search_fields =('city',)

    list_filter = [
        "city",
        "street",
    ]
    


class RecipientAdmin(ModelAdmin):

    list_display = [
        "fname", "lname", "telefon"
    ]
    search_fields =('fname','lname')

class RouteAdmin(ModelAdmin):

    list_display = [
        "id", "addr_city", "adress_Sender", "adress_Recipient"
    ]

    @admin.display(description='Город отправителя')
    def addr_city(self, obj):
        return '{}'.format(obj.adress_Sender.city)
    

    search_fields =('adress_Sender__city','adress_Recipient__city')

class ContractAdmin(ModelAdmin):
    list_display =[
        "client","recipient","manager","driver","creation_date","closing_date"
    ]
    search_fields =('client','manager','driver','creation_date','closing_date')

    list_filter = [
        "manager",
        "driver",
        "creation_date",
        "closing_date"
    ]

admin.site.register(Contract,ContractAdmin)
admin.site.register(Recipient,RecipientAdmin)
admin.site.register(AdressSender, AdressSenderAdmin)
admin.site.register(AdressRecipient, AdressRecipientAdmin)
admin.site.register(Route,RouteAdmin)



