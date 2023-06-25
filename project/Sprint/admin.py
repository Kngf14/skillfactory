from django.contrib import admin

from .models import User, Coords, Level, Mountain, ImagesOfMountains

admin.site.register(User)
admin.site.register(Coords)
admin.site.register(Level)
admin.site.register(Mountain)
admin.site.register(ImagesOfMountains)
