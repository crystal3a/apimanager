from django.contrib import admin
from .models import Dreyeendetail, Dreyemainen
# Register your models here.


@admin.register(Dreyemainen)
class DreyemainenAdmin(admin.ModelAdmin):
    class Meta:
        pass


@admin.register(Dreyeendetail)
class DreyeendetailAdmin(admin.ModelAdmin):
    class Meta:
        pass
