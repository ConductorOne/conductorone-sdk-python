"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from sdk import utils
from sdk._hooks import HookContext
from sdk.models import errors, operations, shared
from sdk.types import BaseModel, OptionalNullable, UNSET
from typing import Optional, Union, cast

class Apps(BaseSDK):
    
    
    def create(
        self, *,
        request: Optional[Union[shared.CreateAppRequest, shared.CreateAppRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsCreateResponse:
        r"""Create

        Create a new app.

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
            request = utils.unmarshal(request, shared.CreateAppRequest)
        request = cast(shared.CreateAppRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/api/v1/apps",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[shared.CreateAppRequest]),
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.Create", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsCreateResponse(create_app_response=utils.unmarshal_json(http_res.text, Optional[shared.CreateAppResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def create_async(
        self, *,
        request: Optional[Union[shared.CreateAppRequest, shared.CreateAppRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsCreateResponse:
        r"""Create

        Create a new app.

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
            request = utils.unmarshal(request, shared.CreateAppRequest)
        request = cast(shared.CreateAppRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/api/v1/apps",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, True, "json", Optional[shared.CreateAppRequest]),
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.Create", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsCreateResponse(create_app_response=utils.unmarshal_json(http_res.text, Optional[shared.CreateAppResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def delete(
        self, *,
        request: Union[operations.C1APIAppV1AppsDeleteRequest, operations.C1APIAppV1AppsDeleteRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsDeleteResponse:
        r"""Delete

        Delete an app.

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
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.C1APIAppV1AppsDeleteRequest)
        request = cast(operations.C1APIAppV1AppsDeleteRequest, request)
        
        req = self.build_request(
            method="DELETE",
            path="/api/v1/apps/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.delete_app_request, False, True, "json", Optional[shared.DeleteAppRequest]),
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.Delete", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsDeleteResponse(delete_app_response=utils.unmarshal_json(http_res.text, Optional[shared.DeleteAppResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def delete_async(
        self, *,
        request: Union[operations.C1APIAppV1AppsDeleteRequest, operations.C1APIAppV1AppsDeleteRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsDeleteResponse:
        r"""Delete

        Delete an app.

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
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.C1APIAppV1AppsDeleteRequest)
        request = cast(operations.C1APIAppV1AppsDeleteRequest, request)
        
        req = self.build_request(
            method="DELETE",
            path="/api/v1/apps/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.delete_app_request, False, True, "json", Optional[shared.DeleteAppRequest]),
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.Delete", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsDeleteResponse(delete_app_response=utils.unmarshal_json(http_res.text, Optional[shared.DeleteAppResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def get(
        self, *,
        request: Union[operations.C1APIAppV1AppsGetRequest, operations.C1APIAppV1AppsGetRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsGetResponse:
        r"""Get

        Get an app by ID.

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
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.C1APIAppV1AppsGetRequest)
        request = cast(operations.C1APIAppV1AppsGetRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/api/v1/apps/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.Get", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsGetResponse(get_app_response=utils.unmarshal_json(http_res.text, Optional[shared.GetAppResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def get_async(
        self, *,
        request: Union[operations.C1APIAppV1AppsGetRequest, operations.C1APIAppV1AppsGetRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsGetResponse:
        r"""Get

        Get an app by ID.

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
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.C1APIAppV1AppsGetRequest)
        request = cast(operations.C1APIAppV1AppsGetRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/api/v1/apps/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.Get", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsGetResponse(get_app_response=utils.unmarshal_json(http_res.text, Optional[shared.GetAppResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def list(
        self, *,
        request: Optional[Union[operations.C1APIAppV1AppsListRequest, operations.C1APIAppV1AppsListRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsListResponse:
        r"""List

        List all apps.

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
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.C1APIAppV1AppsListRequest)
        request = cast(operations.C1APIAppV1AppsListRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/api/v1/apps",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.List", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsListResponse(list_apps_response=utils.unmarshal_json(http_res.text, Optional[shared.ListAppsResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def list_async(
        self, *,
        request: Optional[Union[operations.C1APIAppV1AppsListRequest, operations.C1APIAppV1AppsListRequestTypedDict]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsListResponse:
        r"""List

        List all apps.

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
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.C1APIAppV1AppsListRequest)
        request = cast(operations.C1APIAppV1AppsListRequest, request)
        
        req = self.build_request(
            method="GET",
            path="/api/v1/apps",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.List", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsListResponse(list_apps_response=utils.unmarshal_json(http_res.text, Optional[shared.ListAppsResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def update(
        self, *,
        request: Union[operations.C1APIAppV1AppsUpdateRequest, operations.C1APIAppV1AppsUpdateRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsUpdateResponse:
        r"""Update

        Update an existing app.

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
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.C1APIAppV1AppsUpdateRequest)
        request = cast(operations.C1APIAppV1AppsUpdateRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/api/v1/apps/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.update_app_request, False, True, "json", Optional[shared.UpdateAppRequest]),
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.Update", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsUpdateResponse(update_app_response=utils.unmarshal_json(http_res.text, Optional[shared.UpdateAppResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def update_async(
        self, *,
        request: Union[operations.C1APIAppV1AppsUpdateRequest, operations.C1APIAppV1AppsUpdateRequestTypedDict],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> operations.C1APIAppV1AppsUpdateResponse:
        r"""Update

        Update an existing app.

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
        
        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.C1APIAppV1AppsUpdateRequest)
        request = cast(operations.C1APIAppV1AppsUpdateRequest, request)
        
        req = self.build_request(
            method="POST",
            path="/api/v1/apps/{id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request.update_app_request, False, True, "json", Optional[shared.UpdateAppRequest]),
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
            hook_ctx=HookContext(operation_id="c1.api.app.v1.Apps.Update", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return operations.C1APIAppV1AppsUpdateResponse(update_app_response=utils.unmarshal_json(http_res.text, Optional[shared.UpdateAppResponse]), status_code=http_res.status_code, content_type=http_res.headers.get("Content-Type") or "", raw_response=http_res)
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
