"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import directoryview as shared_directoryview
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Any, Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DirectoryServiceListResponseExpanded:
    r"""Contains an arbitrary serialized message along with a @type that describes the type of the serialized message."""
    at_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('@type'), 'exclude': lambda f: f is None }})
    r"""The type of the serialized message."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DirectoryServiceListResponse:
    r"""The DirectoryServiceListResponse message contains a list of results and a nextPageToken if applicable."""
    expanded: Optional[List[DirectoryServiceListResponseExpanded]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expanded') }})
    r"""The nextPageToken is shown for the next page if the number of results is larger than the max page size.
     The server returns one page of results and the nextPageToken until all results are retreived.
     To retrieve the next page, use the same request and append a pageToken field with the value of nextPageToken shown on the previous page.
    """
    list: Optional[List[shared_directoryview.DirectoryView]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list') }})
    r"""The list of results containing up to X results, where X is the page size defined in the request."""
    next_page_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nextPageToken'), 'exclude': lambda f: f is None }})
    r"""List of serialized related objects."""
    

