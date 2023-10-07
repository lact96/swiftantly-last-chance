from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Workspace)
admin.site.register(CustomUser)
admin.site.register(VirtualDomain)
admin.site.register(EmailUser)