"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AppUserExpandMask:
    r"""The AppUserExpandMask message contains a list of paths to expand in the response."""
    paths: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paths') }})
    r"""The paths to expand in the response. May be any combination of \\"*\\", \\"identity_user_id\\", \\"app_id\\", and \\"last_usage\\"."""
    

