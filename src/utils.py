"""
Utility functions for common application tasks.
"""


def send_notification(user: str, message: str) -> bool:
    """
    Send a notification to a user.

    This is a placeholder implementation that simply prints the
    notification and returns True to indicate success.

    Args:
        user: The recipient identifier (e.g., username or email).
        message: The notification message.

    Returns:
        True if the notification was "sent".
    """
    print(f"[Notification] To: {user}")
    print(f"Message: {message}")
    return True


if __name__ == "__main__":
    send_notification("alice@example.com", "Your report is ready.")