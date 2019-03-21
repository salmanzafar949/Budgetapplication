from ApiApp.api.viewsets import BlogViewSets
from rest_framework import routers

router = routers.DefaultRouter()

router.register('blog', BlogViewSets, base_name='blog')