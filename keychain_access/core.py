from __future__ import annotations

from keychain_access.exceptions import KeychainError
from Foundation import NSMutableDictionary
from Security import (
    SecItemAdd,
    SecItemCopyMatching,
    SecItemDelete,
    kSecClass,
    kSecClassGenericPassword,
    kSecAttrService,
    kSecAttrAccount,
    kSecValueData,
    kSecReturnData,
    kSecMatchLimit,
    kSecMatchLimitOne,
)


def add(account: str, service: str, password: str | bytes) -> None:
    """Add a password to the keychain.

    Args:
        account: The account name.
        service: The service name.
        password: The password, as either a string or bytes.

    Returns:
        The status code.

    Raises:
        KeychainError: If the item could not be added.

    Examples:
        >>> keychain_access.add("my_account", "my_service", "my_password")

        >>> keychain_access.add("my_account", "my_service", b"my_password")
    """
    query = NSMutableDictionary.dictionary()
    query[kSecClass] = kSecClassGenericPassword
    query[kSecAttrAccount] = account
    query[kSecAttrService] = service
    query[kSecValueData] = password.encode() if isinstance(password, str) else password

    try:
        status = SecItemAdd(query, None)
    except Exception as e:
        raise KeychainError(str(e)) from e

    if status != 0:
        raise KeychainError(f"Failed to add item to keychain (status={status})")


def find(account: str, service: str) -> str | None:
    """Find a password in the keychain.

    Args:
        account: The account name.
        service: The service name.

    Returns:
        The password, or `None` if not found.

    Raises:
        KeychainError: If an internal error occurred.

    Examples:
        >>> keychain_access.find("my_account", "my_service")
        "my_password"

        >>> keychain_access.find("my_account", "my_service")
        b"my_password"
    """
    query = NSMutableDictionary.dictionary()
    query[kSecClass] = kSecClassGenericPassword
    query[kSecAttrAccount] = account
    query[kSecAttrService] = service
    query[kSecReturnData] = True
    query[kSecMatchLimit] = kSecMatchLimitOne

    try:
        data, _ = SecItemCopyMatching(query, None)
    except Exception as e:
        raise KeychainError(str(e)) from e

    return data.bytes().tobytes().decode() if data is not None else None


def delete(account: str, service: str) -> None:
    """Delete a password from the keychain.

    Args:
        account: The account name.
        service: The service name.

    Returns:
        The status code.

    Raises:
        KeychainError: If the item could not be deleted.

    Examples:
        >>> keychain_access.delete("my_account", "my_service")
    """
    query = NSMutableDictionary.dictionary()
    query[kSecClass] = kSecClassGenericPassword
    query[kSecAttrAccount] = account
    query[kSecAttrService] = service

    try:
        status = SecItemDelete(query)
    except Exception as e:
        raise KeychainError(str(e)) from e

    if status != 0:
        raise KeychainError(f"Failed to delete item from keychain (status={status})")
