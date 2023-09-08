"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import provisionpolicy as shared_provisionpolicy
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from sdk import utils
from typing import Optional



@dataclasses.dataclass
class AppEntitlementDurationUnset:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppEntitlement:
    r"""The app entitlement represents one permission in a downstream App (SAAS) that can be granted. For example, GitHub Read vs GitHub Write.

    This message contains a oneof named max_grant_duration. Only a single field of the following list may be set at a time:
      - durationUnset
      - durationGrant
    """
    alias: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alias'), 'exclude': lambda f: f is None }})
    r"""The alias of the app entitlement used by Cone. Also exact-match queryable."""
    app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app that is associated with the app entitlement."""
    app_resource_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResourceId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app resource that is associated with the app entitlement"""
    app_resource_type_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResourceTypeId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app resource type that is associated with the app entitlement"""
    certify_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certifyPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the policy that will be used for certify tickets related to the app entitlement."""
    compliance_framework_value_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('complianceFrameworkValueIds'), 'exclude': lambda f: f is None }})
    r"""The IDs of different compliance frameworks associated with this app entitlement ex (SOX, HIPAA, PCI, etc.)"""
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    deleted_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deletedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the app entitlement."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name of the app entitlement."""
    duration_grant: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('durationGrant'), 'exclude': lambda f: f is None }})
    duration_unset: Optional[AppEntitlementDurationUnset] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('durationUnset'), 'exclude': lambda f: f is None }})
    emergency_grant_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emergencyGrantEnabled'), 'exclude': lambda f: f is None }})
    r"""This enables tasks to be created in an emergency and use a selected emergency access policy."""
    emergency_grant_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emergencyGrantPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the policy that will be used for emergency access grant tasks."""
    grant_count: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grantCount'), 'exclude': lambda f: f is None }})
    r"""The amount of grants open for this entitlement"""
    grant_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grantPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the policy that will be used for grant tickets related to the app entitlement."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique ID for the App Entitlement."""
    provision_policy: Optional[shared_provisionpolicy.ProvisionPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provisionerPolicy'), 'exclude': lambda f: f is None }})
    r"""ProvisionPolicy is a oneOf that indicates how a provision step should be processed.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
      - connector
      - manual
      - delegated
    """
    revoke_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revokePolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the policy that will be used for revoke tickets related to the app entitlement"""
    risk_level_value_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('riskLevelValueId'), 'exclude': lambda f: f is None }})
    r"""The riskLevelValueId field."""
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug'), 'exclude': lambda f: f is None }})
    r"""The slug is displayed as an oval next to the name in the frontend of C1, it tells you what permission the entitlement grants. See https://www.conductorone.com/docs/product/manage-access/entitlements/"""
    system_builtin: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('systemBuiltin'), 'exclude': lambda f: f is None }})
    r"""This field indicates if this is a system builtin entitlement."""
    updated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AppEntitlementInput:
    r"""The app entitlement represents one permission in a downstream App (SAAS) that can be granted. For example, GitHub Read vs GitHub Write.

    This message contains a oneof named max_grant_duration. Only a single field of the following list may be set at a time:
      - durationUnset
      - durationGrant
    """
    app_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app that is associated with the app entitlement."""
    app_resource_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResourceId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app resource that is associated with the app entitlement"""
    app_resource_type_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appResourceTypeId'), 'exclude': lambda f: f is None }})
    r"""The ID of the app resource type that is associated with the app entitlement"""
    certify_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certifyPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the policy that will be used for certify tickets related to the app entitlement."""
    compliance_framework_value_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('complianceFrameworkValueIds'), 'exclude': lambda f: f is None }})
    r"""The IDs of different compliance frameworks associated with this app entitlement ex (SOX, HIPAA, PCI, etc.)"""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""The description of the app entitlement."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName'), 'exclude': lambda f: f is None }})
    r"""The display name of the app entitlement."""
    duration_grant: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('durationGrant'), 'exclude': lambda f: f is None }})
    duration_unset: Optional[AppEntitlementDurationUnset] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('durationUnset'), 'exclude': lambda f: f is None }})
    emergency_grant_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emergencyGrantEnabled'), 'exclude': lambda f: f is None }})
    r"""This enables tasks to be created in an emergency and use a selected emergency access policy."""
    emergency_grant_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emergencyGrantPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the policy that will be used for emergency access grant tasks."""
    grant_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grantPolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the policy that will be used for grant tickets related to the app entitlement."""
    provision_policy: Optional[shared_provisionpolicy.ProvisionPolicy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provisionerPolicy'), 'exclude': lambda f: f is None }})
    r"""ProvisionPolicy is a oneOf that indicates how a provision step should be processed.

    This message contains a oneof named typ. Only a single field of the following list may be set at a time:
      - connector
      - manual
      - delegated
    """
    revoke_policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revokePolicyId'), 'exclude': lambda f: f is None }})
    r"""The ID of the policy that will be used for revoke tickets related to the app entitlement"""
    risk_level_value_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('riskLevelValueId'), 'exclude': lambda f: f is None }})
    r"""The riskLevelValueId field."""
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug'), 'exclude': lambda f: f is None }})
    r"""The slug is displayed as an oval next to the name in the frontend of C1, it tells you what permission the entitlement grants. See https://www.conductorone.com/docs/product/manage-access/entitlements/"""
    

