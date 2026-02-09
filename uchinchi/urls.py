from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (Salom1vset, Salom2vset, Salom3vset, Salom4vset, Salom5vset)






router = DefaultRouter()
router.register(r"1", Salom1vset)
router.register(r"2", Salom2vset)
router.register(r"3", Salom3vset)
router.register(r"4", Salom4vset)
router.register(r"5", Salom5vset)



urlpatterns = [
    path("", include(router.urls)),
]
