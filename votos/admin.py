# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (Votos,Candidato,Distrito)

# TODO Register your models here.
admin.site.register(Votos)
admin.site.register(Candidato)
admin.site.register(Distrito)
