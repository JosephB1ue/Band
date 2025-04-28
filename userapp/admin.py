from django.contrib import admin
from . models import Register_table, Carttable, Band

# Register your models here.
admin.site.register(Register_table)
admin.site.register(Band)
admin.site.register(Carttable)