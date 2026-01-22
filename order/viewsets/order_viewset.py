from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.all().order_by('id')
