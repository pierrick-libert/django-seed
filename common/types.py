"""A list of custom type"""

from typing import TypedDict

from django.core.paginator import Page
from django.forms import ModelForm


class CustomConditionType(TypedDict):
    """Type dict for condition"""

    condition: bool


class CustomFormType(TypedDict):
    """Type dict for form"""

    form: ModelForm


class CustomPageType(TypedDict):
    """Type dict for pagination"""

    page_obj: Page


class CustomHeadCellType(TypedDict):
    """Type dict for Head Cell Ordering"""

    title: str
    field: str
    arrow_class: str | None
    ordering_fields: str
    order_by: str


class CustomLogInfoType(TypedDict):
    """Type dict for Log Info middleware"""

    remote_address: str
    user_agent: str
    server_hostname: str
    request_method: str
    request_path: str
    execution_time: str
    response_code: str | None
