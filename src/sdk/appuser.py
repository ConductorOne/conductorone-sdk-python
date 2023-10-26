"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from sdk import utils
from sdk.models import errors, operations, shared
from typing import Optional

class AppUser:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def update(self, request: operations.C1APIAppV1AppUserServiceUpdateRequest) -> operations.C1APIAppV1AppUserServiceUpdateResponse:
        r"""Update
        Update an app user by ID. Only the fields specified in the update mask are updated.
         Currently, only the appUserType, and identityUserId fields can be updated.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.C1APIAppV1AppUserServiceUpdateRequest, base_url, '/api/v1/apps/{app_user_app_id}/app_users/{app_user_id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "app_user_service_update_request_input", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.C1APIAppV1AppUserServiceUpdateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AppUserServiceUpdateResponse])
                res.app_user_service_update_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    