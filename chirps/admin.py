from django.contrib import admin

# Register your models here.
from .models import Chirp

class ChirpAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Chirp

admin.site.register(Chirp, ChirpAdmin)