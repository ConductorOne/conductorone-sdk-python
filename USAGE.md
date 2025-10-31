<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from sdk import SDK
from sdk.models import shared


with SDK(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
        oauth="<YOUR_OAUTH_HERE>",
    ),
) as s_client:

    res = s_client.access_conflict.create_monitor(request={
        "display_name": "Hermina.Larkin",
    })

    assert res.conflict_monitor is not None

    # Handle response
    print(res.conflict_monitor)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from sdk import SDK
from sdk.models import shared

async def main():

    async with SDK(
        security=shared.Security(
            bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
            oauth="<YOUR_OAUTH_HERE>",
        ),
    ) as s_client:

        res = await s_client.access_conflict.create_monitor_async(request={
            "display_name": "Hermina.Larkin",
        })

        assert res.conflict_monitor is not None

        # Handle response
        print(res.conflict_monitor)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->