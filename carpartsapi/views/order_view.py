import logging
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from carpartsapi.helper.helper import get_cart_object, get_order_object
from carpartsapi.models.order_model import Order
from carpartsapi.serializers.order_serializer import OrderSerializer


class OrderListApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.is_superuser:
            orders = Order.objects.filter()
        else:
            orders = Order.objects.filter(user=request.user.id)
        serializer = OrderSerializer(orders, many=True)
        self.logger.debug("entering to the get orders list view")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        cart_items_list = request.data.get('items')
        self.logger.debug("entering to the create order view")
        cost = 0
        if cart_items_list is not None and cart_items_list != []:
            for cart_item in cart_items_list:
                cost = cost + cart_item["total_cost"]

            data = {
                'user': request.user.id,
                'customer': request.data.get('customer'),
                'email': request.data.get('email'),
                'phone': request.data.get('phone'),
                'address': request.data.get('address'),
                'total_payment': cost,
                'delivery_date': request.data.get('delivery_date'),
                'delivery_time': request.data.get('delivery_time'),
            }
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                for cart_item in cart_items_list:
                    cart_id = cart_item["id"]
                    cart_instance = get_cart_object(cart_id)
                    if cart_instance is not None:
                        cart_instance.delete()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"response": "unable to make order without product list"}, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, order_id):
        order_instance = get_order_object(order_id)
        self.logger.debug("entering to the get order detail view")
        if not order_instance:
            return Response({"response": "Order with order id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = OrderSerializer(order_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
