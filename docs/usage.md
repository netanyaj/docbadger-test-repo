# Notification Utility

The `src/utils.py` module provides a simple helper function for sending
notifications.

## Function

### `send_notification(user, message)`

Sends a notification to the specified user.

- `user`: The recipient identifier (for example, a username or email address).
- `message`: The notification text to deliver.

The current implementation is a placeholder that prints the notification to the
console and returns `True` to indicate success. In a production application,
this function could be extended to integrate with services such as email, SMS,
push notifications, or messaging platforms.

## Example

```python
from src.utils import send_notification

send_notification(
    "alice@example.com",
    "Your report is ready."
)
```

## Expected Output

```text
[Notification] To: alice@example.com
Message: Your report is ready.
```