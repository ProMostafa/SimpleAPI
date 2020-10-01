
from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import UsersAccounts , ClientsOrder

router=DefaultRouter()
router.register("UsersAccounts",UsersAccounts)
router.register("ClientsOrder",ClientsOrder)
urlpatterns = [
    path("",include(router.urls))
]
