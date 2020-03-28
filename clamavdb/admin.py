from django.contrib import admin

from .models import Signature
from .models import Category

admin.site.register(Signature)
admin.site.register(Category)

