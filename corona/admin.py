from django.contrib import admin

from .models import SubmittedCoronaCase, CoronaCase

admin.site.register(SubmittedCoronaCase)
admin.site.register(CoronaCase)
