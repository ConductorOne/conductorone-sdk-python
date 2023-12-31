"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .facetrange import FacetRange
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FacetRangeItem:
    r"""The FacetRangeItem message."""
    ranges: Optional[List[FacetRange]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ranges') }})
    r"""An array of facet ranges."""
    

