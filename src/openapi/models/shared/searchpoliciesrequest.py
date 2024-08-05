"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .policyref import PolicyRef, PolicyRefTypedDict
from enum import Enum
from openapi.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PolicyTypes(str, Enum):
    POLICY_TYPE_UNSPECIFIED = "POLICY_TYPE_UNSPECIFIED"
    POLICY_TYPE_GRANT = "POLICY_TYPE_GRANT"
    POLICY_TYPE_REVOKE = "POLICY_TYPE_REVOKE"
    POLICY_TYPE_CERTIFY = "POLICY_TYPE_CERTIFY"
    POLICY_TYPE_ACCESS_REQUEST = "POLICY_TYPE_ACCESS_REQUEST"
    POLICY_TYPE_PROVISION = "POLICY_TYPE_PROVISION"

class SearchPoliciesRequestTypedDict(TypedDict):
    r"""Search Policies by a few properties."""
    
    display_name: NotRequired[str]
    r"""Search for policies with a case insensitive match on the display name."""
    include_deleted: NotRequired[bool]
    r"""The includeDeleted field."""
    page_size: NotRequired[int]
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: NotRequired[str]
    r"""The pageToken field."""
    policy_types: NotRequired[Nullable[List[PolicyTypes]]]
    r"""The policy type to search on. This can be POLICY_TYPE_GRANT, POLICY_TYPE_REVOKE, POLICY_TYPE_CERTIFY, POLICY_TYPE_ACCESS_REQUEST, or POLICY_TYPE_PROVISION."""
    query: NotRequired[str]
    r"""Query the policies with a fuzzy search on display name and description."""
    refs: NotRequired[Nullable[List[PolicyRefTypedDict]]]
    r"""The refs field."""
    

class SearchPoliciesRequest(BaseModel):
    r"""Search Policies by a few properties."""
    
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""Search for policies with a case insensitive match on the display name."""
    include_deleted: Annotated[Optional[bool], pydantic.Field(alias="includeDeleted")] = None
    r"""The includeDeleted field."""
    page_size: Annotated[Optional[int], pydantic.Field(alias="pageSize")] = None
    r"""The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)"""
    page_token: Annotated[Optional[str], pydantic.Field(alias="pageToken")] = None
    r"""The pageToken field."""
    policy_types: Annotated[OptionalNullable[List[PolicyTypes]], pydantic.Field(alias="policyTypes")] = UNSET
    r"""The policy type to search on. This can be POLICY_TYPE_GRANT, POLICY_TYPE_REVOKE, POLICY_TYPE_CERTIFY, POLICY_TYPE_ACCESS_REQUEST, or POLICY_TYPE_PROVISION."""
    query: Optional[str] = None
    r"""Query the policies with a fuzzy search on display name and description."""
    refs: OptionalNullable[List[PolicyRef]] = UNSET
    r"""The refs field."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["displayName", "includeDeleted", "pageSize", "pageToken", "policyTypes", "query", "refs"]
        nullable_fields = ["policyTypes", "refs"]
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
        