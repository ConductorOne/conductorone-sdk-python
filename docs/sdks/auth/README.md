# Auth
(*auth*)

### Available Operations

* [introspect](#introspect) - Introspect

## introspect

Introspect returns the current user's principle_id, user_id and a list of roles, permissions, and enabled features.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    security=shared.Security(
        bearer_auth="",
        oauth="",
    ),
)


res = s.auth.introspect()

if res.introspect_response is not None:
    # handle response
```


### Response

**[operations.C1APIAuthV1AuthIntrospectResponse](../../models/operations/c1apiauthv1authintrospectresponse.md)**

