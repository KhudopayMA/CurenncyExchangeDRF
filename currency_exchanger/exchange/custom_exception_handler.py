from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if isinstance(response, Response):
        return response

    if isinstance(exc, IntegrityError):
        custom_response_data = {
            'detail': str(exc)
        }
        response = Response(
            data=custom_response_data,
            status=status.HTTP_409_CONFLICT
        )
        # response.data = custom_response_data
        # response.status_code = status.HTTP_409_CONFLICT
    else:
        response = Response(
            data="Internal Server Error",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return response

