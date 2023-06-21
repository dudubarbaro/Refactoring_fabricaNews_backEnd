from django.contrib import admin

from feeling.models import (
    NewsFeel,
    Feeling,

)

admin.site.register(NewsFeel)
admin.site.register(Feeling)

