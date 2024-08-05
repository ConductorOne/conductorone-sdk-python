<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from openapi import SDK
from openapi.models import shared

s = SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
)


res = s.apps.create()

if res.create_app_response is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from openapi import SDK
from openapi.models import shared

async def main():
    s = SDK(
        security=shared.Security(
            bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
            oauth="<YOUR_OAUTH_HERE>",
        ),
    )
    res = await s.apps.create_async()
    if res.create_app_response is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->