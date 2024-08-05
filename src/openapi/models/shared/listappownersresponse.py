"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .user import User, UserTypedDict
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListAppOwnersResponseTypedDict(TypedDict):
    r"""The ListAppOwnersResponse message."""
    
    list: NotRequired[Nullable[List[UserTypedDict]]]
    r"""The list of results containing up to X results, where X is the page size defined in the request"""
    next_page_token: NotRequired[str]
    r"""The nextPageToken is shown for the next page if the number of results is larger than the max page size. The server returns one page of results and the nextPageToken until all results are retreived. To retrieve the next page, use the same request and append a pageToken field with the value of nextPageToken shown on the previous page."""
    

class ListAppOwnersResponse(BaseModel):
    r"""The ListAppOwnersResponse message."""
    
    list: OptionalNullable[List[User]] = UNSET
    r"""The list of results containing up to X results, where X is the page size defined in the request"""
    next_page_token: Annotated[Optional[str], pydantic.Field(alias="nextPageToken")] = None
    r"""The nextPageToken is shown for the next page if the number of results is larger than the max page size. The server returns one page of results and the nextPageToken until all results are retreived. To retrieve the next page, use the same request and append a pageToken field with the value of nextPageToken shown on the previous page."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["list", "nextPageToken"]
        nullable_fields = ["list"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields
                or (
                    k in optional_fields
                    and k in nullable_fields
                    and (
                        self.__pydantic_fields_set__.intersection({n})
                        or k in null_default_fields
                    )  # pylint: disable=no-member
                )
            ):
                m[k] = val

        return m
        