from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

router = DefaultRouter()

router.register('blogposts', BlogPostViewSet, basename='blogposts')

urlpatterns = router.urls