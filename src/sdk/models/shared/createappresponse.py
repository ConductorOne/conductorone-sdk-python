"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import app as shared_app
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateAppResponse:
    r"""Returns the new app's values."""
    app: Optional[shared_app.App] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app'), 'exclude': lambda f: f is None }})
    r"""The App object provides all of the details for an app, as well as some configuration."""
    

