from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response

from exchange.exceptions import DatabaseOperationException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if isinstance(response, Response):
        return response

    if isinstance(exc, DatabaseOperationException):
        custom_response_data = {
            'message': str(exc)
        }
        response = Response(
            data=custom_response_data,
            status=status.HTTP_409_CONFLICT
        )
    else:
        response = Response(
            data={"message": "Internal Server Error"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response

