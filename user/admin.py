from django.contrib import admin

from user.models import (
    User,
    UserInteractions,
    UserProjectFollow,
)

admin.site.register(User)
admin.site.register(UserInteractions)
admin.site.register(UserProjectFollow)
