"""
Middleware to log all requests and responses.
Uses a logger configured by the name of django.request
to log all requests and responses according to configuration
specified for django.request.
"""

import json
import logging
import socket
import time
from typing import Callable

from django.core.handlers.wsgi import WSGIRequest
from django.template.response import TemplateResponse

from common.types import CustomLogInfoType

REQUEST_LOGGER = logging.getLogger("django.request")


class RequestLogMiddleware:
    """Request Logging Middleware"""

    def __init__(self, get_response: Callable):
        """Constructor"""
        self.get_response = get_response

    def __call__(self, request: WSGIRequest) -> TemplateResponse:
        """Overrides __call__"""
        RequestLogMiddleware.process_request(request)
        response = self.get_response(request)
        RequestLogMiddleware.process_response(request, response)
        return response

    @staticmethod
    def process_request(request: WSGIRequest) -> None:
        """Set Request Start Time to measure time taken to service request"""
        request.start_time = time.time()

    @staticmethod
    def extract_log_info(request: WSGIRequest, response: TemplateResponse = None) -> CustomLogInfoType:
        """Extract appropriate log info from requests/responses/exceptions"""
        log_data: CustomLogInfoType = {
            "remote_address": request.META.get("REMOTE_ADDR", "-"),
            "user_agent": request.headers.get("user-agent", "-"),
            "server_hostname": socket.gethostname(),
            "request_method": request.method,
            "request_path": request.get_full_path(),
            "execution_time": f"{(time.time() - request.start_time):.2f} sec",
            "response_code": None,
        }
        if response:
            log_data["response_code"] = response.status_code

        return log_data

    @staticmethod
    def process_response(request: WSGIRequest, response: TemplateResponse) -> None:
        """Log data using logger"""
        log_data = RequestLogMiddleware.extract_log_info(request=request, response=response)

        if response.status_code in range(400, 499):
            REQUEST_LOGGER.warning(msg=json.dumps(log_data))
        elif response.status_code in range(500, 599):
            REQUEST_LOGGER.error(msg=json.dumps(log_data))
        else:
            REQUEST_LOGGER.info(msg=json.dumps(log_data))
