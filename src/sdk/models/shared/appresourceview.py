"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import appresource as shared_appresource
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppResourceView:
    r"""The app resource view returns an app resource with paths for items in the expand mask filled in when this response is returned and a request expand mask has \\"*\\" or \\"app_id\\" or \\"resource_type_id\\"."""
    app_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appPath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the App object in the array"""
    app_resource: Optional[shared_appresource.AppResource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResource'), 'exclude': lambda f: f is None }})
    r"""The app resource message is a single resource that can have entitlements."""
    resource_type_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resourceTypePath'), 'exclude': lambda f: f is None }})
    r"""JSONPATH expression indicating the location of the Resource Type object in the array"""
    

