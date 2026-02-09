from django.contrib import admin
from .models import Books
from .models import Readers

# Register your models here.
admin.site.register(Books)
admin.site.register(Readers)
