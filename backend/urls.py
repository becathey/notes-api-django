from django.contrib import admin
from django.urls import path, include
from note import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'notes', views.NoteView, 'note')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
