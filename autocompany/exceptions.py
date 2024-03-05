from rest_framework.exceptions import APIException
from rest_framework import status


class BaseCarApiException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, code, error, description):
        self.detail = {'code': code, 'error': error, 'description': description}


class InternalServerError(BaseCarApiException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR


class InvalidParameterException(BaseCarApiException):
    status_code = status.HTTP_400_BAD_REQUEST


class ParseError(BaseCarApiException):
    status_code = status.HTTP_400_BAD_REQUEST


class ValidationError(BaseCarApiException):
    status_code = status.HTTP_400_BAD_REQUEST
