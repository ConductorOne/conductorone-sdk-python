"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from sdk import utils
from sdk._hooks import HookContext
from sdk.models import errors, operations, shared
from sdk.types import BaseModel, OptionalNullable, UNSET
from typing import Optional, Union, cast

class SessionSettings(BaseSDK):
    
    
    def get(
        self, *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APISettingsV1SessionSettingsServiceGetResponse:
        r"""Get

        Invokes the c1.api.settings.v1.SessionSettingsService.Get method.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/api/v1/settings/session",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="c1.api.settings.v1.SessionSettingsService.Get", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APISettingsV1SessionSettingsServiceGetResponse(get_session_settings_response=utils.unmarshal_json(http_res.text, Optional[shared.GetSessionSettingsResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def get_async(
        self, *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APISettingsV1SessionSettingsServiceGetResponse:
        r"""Get

        Invokes the c1.api.settings.v1.SessionSettingsService.Get method.

        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/api/v1/settings/session",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="c1.api.settings.v1.SessionSettingsService.Get", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APISettingsV1SessionSettingsServiceGetResponse(get_session_settings_response=utils.unmarshal_json(http_res.text, Optional[shared.GetSessionSettingsResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def update(
        self, *,
        request: Optional[Union[shared.UpdateSessionSettingsRequest, shared.UpdateSessionSettingsRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APISettingsV1SessionSettingsServiceUpdateResponse:
        r"""Update

        Invokes the c1.api.settings.v1.SessionSettingsService.Update method.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel) and request is not None:
            request = utils.unmarshal(request, shared.UpdateSessionSettingsRequest)
        request = cast(shared.UpdateSessionSettingsRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/api/v1/settings/session",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[shared.UpdateSessionSettingsRequest]),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="c1.api.settings.v1.SessionSettingsService.Update", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APISettingsV1SessionSettingsServiceUpdateResponse(update_session_settings_response=utils.unmarshal_json(http_res.text, Optional[shared.UpdateSessionSettingsResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def update_async(
        self, *,
        request: Optional[Union[shared.UpdateSessionSettingsRequest, shared.UpdateSessionSettingsRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APISettingsV1SessionSettingsServiceUpdateResponse:
        r"""Update

        Invokes the c1.api.settings.v1.SessionSettingsService.Update method.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        if not isinstance(request, BaseModel) and request is not None:
            request = utils.unmarshal(request, shared.UpdateSessionSettingsRequest)
        request = cast(shared.UpdateSessionSettingsRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/api/v1/settings/session",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[shared.UpdateSessionSettingsRequest]),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="c1.api.settings.v1.SessionSettingsService.Update", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APISettingsV1SessionSettingsServiceUpdateResponse(update_session_settings_response=utils.unmarshal_json(http_res.text, Optional[shared.UpdateSessionSettingsResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
