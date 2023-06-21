from django.contrib import admin

from core.models import (
    Category,
    Comments,
    Favorites,
    Reaction,
    SaveToRead,
    Project,
)


admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Favorites)
admin.site.register(Reaction)
admin.site.register(SaveToRead)
admin.site.register(Project)
