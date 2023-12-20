from rest_framework.viewsets import ModelViewSet
from post.models import Post
from restaurant.models import Menu
from restaurant.models import Client
from restaurant.models import Order
from post.api.serializers import PostSerializer
from post.api.serializers import MenuSerializer
from post.api.serializers import ClientSerializer
from post.api.serializers import OrderSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
class MenuApiViewSet(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
class ClientApiViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class OrderApiViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()