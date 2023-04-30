from django.contrib import admin
from .models import User, Battle,History,Money


admin.site.register(User)
admin.site.register(Battle)
admin.site.register(History)
admin.site.register(Money)