from django.contrib import admin

# Register your models here.

from .models import Persona, Cancha, Horario, Reserva, Pago

admin.site.register(Persona)
admin.site.register(Cancha)
admin.site.register(Horario)
admin.site.register(Reserva)
admin.site.register(Pago)
