"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .connectorexpandmask import ConnectorExpandMask, ConnectorExpandMaskTypedDict
import pydantic
from pydantic import model_serializer
from sdk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ConnectorServiceCreateDelegatedRequestTypedDict(TypedDict):
    r"""The ConnectorServiceCreateDelegatedRequest message contains the fields required to create a connector."""
    
    connector_expand_mask: NotRequired[ConnectorExpandMaskTypedDict]
    r"""The ConnectorExpandMask is used to expand related objects on a connector."""
    catalog_id: NotRequired[str]
    r"""The catalogId describes which catalog entry this connector is an instance of. For example, every Okta connector will have the same catalogId indicating it is an Okta connector."""
    description: NotRequired[str]
    r"""The description of the connector."""
    display_name: NotRequired[str]
    r"""The displayName of the connector."""
    user_ids: NotRequired[Nullable[List[str]]]
    r"""The userIds field is used to define the integration owners of the connector."""
    

class ConnectorServiceCreateDelegatedRequest(BaseModel):
    r"""The ConnectorServiceCreateDelegatedRequest message contains the fields required to create a connector."""
    
    connector_expand_mask: Annotated[Optional[ConnectorExpandMask], pydantic.Field(alias="expandMask")] = None
    r"""The ConnectorExpandMask is used to expand related objects on a connector."""
    catalog_id: Annotated[Optional[str], pydantic.Field(alias="catalogId")] = None
    r"""The catalogId describes which catalog entry this connector is an instance of. For example, every Okta connector will have the same catalogId indicating it is an Okta connector."""
    description: Optional[str] = None
    r"""The description of the connector."""
    display_name: Annotated[Optional[str], pydantic.Field(alias="displayName")] = None
    r"""The displayName of the connector."""
    user_ids: Annotated[OptionalNullable[List[str]], pydantic.Field(alias="userIds")] = UNSET
    r"""The userIds field is used to define the integration owners of the connector."""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["ConnectorExpandMask", "catalogId", "description", "displayName", "userIds"]
        nullable_fields = ["userIds"]
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
        
