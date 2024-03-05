from rest_framework import status
from autocompany.exceptions import BaseCarApiException


class ProductDoesNotExistException(BaseCarApiException):
    status_code = status.HTTP_403_FORBIDDEN


class CartDoesNotExistException(BaseCarApiException):
    status_code = status.HTTP_403_FORBIDDEN


class OrderDoesNotExistException(BaseCarApiException):
    status_code = status.HTTP_403_FORBIDDEN
