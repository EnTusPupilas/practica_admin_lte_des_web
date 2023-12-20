from rest_framework.serializers import ModelSerializer
from post.models import Post
from restaurant.models import Menu
from restaurant.models import Client
from restaurant.models import Order

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image']
        
class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'type', 'img']
        
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'table']
        
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'client', 'menu', 'total', 'amount']