from django.contrib import admin

from .models import Tipo_licencia, Expediente, Barrios, Propietarios, Tipo_usos, Usos, icnonos


admin.site.register(Tipo_licencia)
admin.site.register(Expediente)
admin.site.register(Barrios)
admin.site.register(Propietarios)
admin.site.register(Tipo_usos)
admin.site.register(Usos)
admin.site.register(icnonos)


