
from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import UsersAccounts

router=DefaultRouter()
router.register("UsersAccounts",UsersAccounts)
urlpatterns = [
    path("",include(router.urls))
]
