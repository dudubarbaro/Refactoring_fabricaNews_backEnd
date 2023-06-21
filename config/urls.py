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
    MyTokenObtainPairView,
)

from project.views import (
    NewsViewSet,
)
from feeling.views import (
    FeelingViewSet,
    NewsFeelViewSet,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
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
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include(router.urls)),
]
