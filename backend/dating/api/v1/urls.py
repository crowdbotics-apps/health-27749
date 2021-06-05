from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    SettingViewSet,
    LikeViewSet,
    UserPhotoViewSet,
    MatchViewSet,
    DislikeViewSet,
    InboxViewSet,
    ProfileViewSet,
)

router = DefaultRouter()
router.register("userphoto", UserPhotoViewSet)
router.register("inbox", InboxViewSet)
router.register("dislike", DislikeViewSet)
router.register("like", LikeViewSet)
router.register("profile", ProfileViewSet)
router.register("match", MatchViewSet)
router.register("setting", SettingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
