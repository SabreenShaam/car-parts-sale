import logging
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from carpartsapi.helper.helper import get_product_object
from carpartsapi.serializers.product_serializer import ProductSerializer
from carpartsapi.models.product_model import Product


class ProductListApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.logger.debug("entering to the get product list view")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.user.is_superuser:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                self.logger.debug("entering to the product create view")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        self.logger.error("user permission denied")
        return Response({"response": "Super user only can add a product"}, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):
    logger = logging.getLogger(__name__)
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, product_code):
        product_instance = get_product_object(product_code)
        self.logger.debug("entering to the get product detail view")
        if not product_instance:
            return Response({"response": "Object with product id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, product_code):
        if request.user.is_superuser:
            self.logger.debug("entering to the product update view")
            product_instance = get_product_object(product_code)
            if not product_instance:
                return Response({"response": "Object with project id does not exists"},
                                status=status.HTTP_400_BAD_REQUEST)
            serializer = ProductSerializer(instance=product_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"response": "Super user only can modify product details"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_code):
        if request.user.is_superuser:
            product_instance = get_product_object(product_code)
            self.logger.debug("entering to the product delete view")
            if not product_instance:
                return Response({"response": "Product does not exists"},
                                status=status.HTTP_400_BAD_REQUEST)
            product_instance.delete()
            return Response({"response": "Product deleted Successfully"}, status=status.HTTP_200_OK)
        return Response({"response": "Super user only can delete a product"}, status=status.HTTP_400_BAD_REQUEST)
