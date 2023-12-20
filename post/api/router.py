from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewSet
from post.api.views import MenuApiViewSet
from post.api.views import ClientApiViewSet
from post.api.views import OrderApiViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='post', basename='post', viewset=PostApiViewSet)
router_posts.register(prefix='menu', basename='menu', viewset=MenuApiViewSet)
router_posts.register(prefix='client', basename='client', viewset=ClientApiViewSet)
router_posts.register(prefix='order', basename='order', viewset=OrderApiViewSet)