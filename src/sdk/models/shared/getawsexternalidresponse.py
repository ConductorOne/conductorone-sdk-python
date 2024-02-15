"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .awsexternalid import AWSExternalID
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAWSExternalIDResponse:
    r"""The GetAWSExternalIDResponse message."""
    aws_external_id: Optional[AWSExternalID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsExternalId'), 'exclude': lambda f: f is None }})
    r"""The AWSExternalID message."""
    
