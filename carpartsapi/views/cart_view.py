import logging
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from carpartsapi.helper.helper import get_product_object, get_cart_object
from carpartsapi.models.cart_model import Cart
from carpartsapi.serializers.cart_serializer import CartSerializer


class CartListApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user.id)
        serializer = CartSerializer(carts, many=True)
        self.logger.debug("entering to the get cart list view")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        self.logger.debug("entering to the add cart item view")
        product_code = request.data.get('product_code')
        quantity = request.data.get('quantity')
        if product_code is None or product_code == '':
            return Response({"response": "product_code field is missing"},
                            status=status.HTTP_400_BAD_REQUEST)
        if quantity is None or quantity == '':
            return Response({"response": "quantity field is missing"},
                            status=status.HTTP_400_BAD_REQUEST)
        user = request.user.id
        product_instance = get_product_object(product_code)
        if product_instance is not None:
            available_stock = product_instance.stock
            if available_stock >= quantity:
                unit_price = product_instance.unit_price
                total_cost = unit_price * quantity
                product_instance.stock = product_instance.stock - quantity
                product_instance.save()
                data = {
                    'product_code': product_code,
                    'quantity': quantity,
                    'unit_price': unit_price,
                    'total_cost': total_cost,
                    'user': user
                }

                serializer = CartSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"response": "quantity exceeds than available stock"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"response": "product is not exists"},
                        status=status.HTTP_400_BAD_REQUEST)


class CartDetailApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, cart_id):
        product_instance = get_cart_object(cart_id)
        self.logger.debug("entering to the cart detail view")
        if not product_instance:
            return Response({"response": "Product with product id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CartSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, cart_id, *args, **kwargs):
        cart_instance = get_cart_object(cart_id)
        self.logger.debug("entering to the delete cart item view")
        if not cart_instance:
            return Response({"response": "Cart with cart id does not exists"},status=status.HTTP_400_BAD_REQUEST)
        if cart_instance is not None:
            pro_code = cart_instance.product_code
            product_instance = get_product_object(pro_code)
            product_instance.stock = product_instance.stock + cart_instance.quantity
            product_instance.save()
        cart_instance.delete()
        return Response({"response": "Cart Object deleted successfully"}, status=status.HTTP_200_OK)
