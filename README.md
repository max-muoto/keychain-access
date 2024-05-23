# keychain_access

`keychain_access` is a simple Python library that wraps the objective-c Security framework to access the macOS keychain, allowing you to store and retrieve passwords for your OSX applications. Due to this, `pyobjc` is required as a dependency.

## Installation

```bash
pip install keychain_access
```

## Usage

```python
import keychain_access

# Store a password
keychain_access.set('my_service', 'my_account', 'my_password')

# Retrieve a password
password = keychain_access.get('my_service', 'my_account')

# Delete a password
keychain_access.delete('my_service', 'my_account')
```

## License

MIT
