from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


router.register('members', views.SystemAPI)
router.register('Time', views.TimeAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]