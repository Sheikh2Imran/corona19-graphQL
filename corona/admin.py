from django.contrib import admin

from .models import District, SubmittedCoronaCase, CoronaCase

admin.site.register(District)
admin.site.register(SubmittedCoronaCase)
admin.site.register(CoronaCase)
