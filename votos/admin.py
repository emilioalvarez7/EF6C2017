# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (Distrito,Candidato,Votos)

# Register your models here.
admin.site.register(Distrito)
admin.site.register(Candidato)
admin.site.register(Votos)
