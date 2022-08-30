from .views import UserRegistration
from rest_framework import routers
router = routers.DefaultRouter(trailing_slash=True)
router.register('create', UserRegistration)
