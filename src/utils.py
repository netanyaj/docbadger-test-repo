"""
Utility functions for common application tasks.
"""


def send_notification(
    user: str,
    message: str,
    priority: str = "normal",
) -> bool:
    """
    Send a notification to a user.

    Args:
        user: The recipient identifier.
        message: The notification message.
        priority: Notification priority ("low", "normal", or "high").

    Returns:
        True if the notification was "sent".
    """
    print(f"[{priority.upper()}] Notification")
    print(f"To: {user}")
    print(f"Message: {message}")
    return True


if __name__ == "__main__":
    send_notification(
        "alice@example.com",
        "Your report is ready.",
        priority="high",
    )