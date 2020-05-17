from django.contrib import admin

# Register your models here.
from .models import Chirp, ChirpLike


class ChirpLikeAdmin(admin.TabularInline):
    model = ChirpLike

class ChirpAdmin(admin.ModelAdmin):
    inlines = [ChirpLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user__username', 'user__email']
    class Meta:
        model = Chirp

admin.site.register(Chirp, ChirpAdmin)