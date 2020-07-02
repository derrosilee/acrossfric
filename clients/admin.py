from django.contrib import admin
from .models import Clients, Claims

# Register your models here.

class  ClientsAdmin(admin.ModelAdmin):
    list_display = ("Name", 'Class_insured', 'Car_plate',  'Insuerer', "Policy_no", "Date_insured", "Date_expiry", "Rate", "Sum_insured", "Annual_premium", "Commision") 
    search_fields = ("Name", "Insuerer")

admin.site.site_header = "Accros Africa Insurance Agency CMS"
admin.site.register(Clients, ClientsAdmin)

class ClaimsAdmin(admin.ModelAdmin):
    list_display = ("Name", "Class_insurance", "Policy_no", "Claim_no", "Date_Accident", "Place", "Explanation")
    search_fields = ("Name", "Claim_no")

admin.site.register(Claims, ClaimsAdmin)