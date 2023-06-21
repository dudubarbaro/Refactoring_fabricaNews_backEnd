from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import (
    CategoryViewSet,
    FavoritesViewSet,
    SaveToReadViewSet,
    CommentsViewSet,
    ReactionViewSet
)
from user.views import (
    UserProjectFollowViewSet,
)

from project.views import (
    NewsViewSet,
)
from feeling.views import (
    FeelingViewSet,
    NewsFeelViewSet,
)
router = DefaultRouter()
router.register(r"newsfeel", NewsFeelViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"favorites", FavoritesViewSet)
router.register(r"feelings", FeelingViewSet)
router.register(r"news", NewsViewSet)
router.register(r"userProjectFollows", UserProjectFollowViewSet)
router.register(r"savetoread", SaveToReadViewSet)
router.register(r"reactions", ReactionViewSet)
router.register(r"comments", CommentsViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
