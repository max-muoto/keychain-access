"""Interact with the macOS keychain from Python.

```python
import keychain_access

# Store a password
keychain_access.set("my_service", "my_account", "my_password")

# Retrieve a password
password = keychain_access.get("my_service", "my_account")

# Delete a password
keychain_access.delete("my_service", "my_account")
```
"""

from __future__ import annotations

from keychain_access.core import add, delete, get

__all__ = ["add", "get", "delete"]
