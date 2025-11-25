<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from conductorone_sdk import SDK
from conductorone_sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as sdk:

    res = sdk.access_conflict.create_monitor()

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from conductorone_sdk import SDK
from conductorone_sdk.models import shared

async def main():

    async with SDK(
        security=shared.Security(
            bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
            oauth="<YOUR_OAUTH_HERE>",
        ),
    ) as sdk:

        res = await sdk.access_conflict.create_monitor_async()

        assert res.conflict_monitor is not None

        # Handle response
        print(res.conflict_monitor)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->