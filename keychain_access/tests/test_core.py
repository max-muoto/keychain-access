from __future__ import annotations

import contextlib

import pytest

import keychain_access
from keychain_access.exceptions import KeychainError


@pytest.fixture(autouse=True)
def cleanup():
    """Ensure the keychain is clean before and after each test."""
    with contextlib.suppress(KeychainError):
        keychain_access.delete("my_account", "my_service")


def test_keychain_access():
    """Test general E2E functionality."""
    keychain_access.add("my_account", "my_service", "my_password")
    assert keychain_access.find("my_account", "my_service") == "my_password"

    keychain_access.delete("my_account", "my_service")
    assert keychain_access.find("my_account", "my_service") is None


def test_keychain_access_error():
    """Test error handling."""
    with pytest.raises(KeychainError):
        keychain_access.delete("my_account", "my_service")

    # Add the password
    keychain_access.add("my_account", "my_service", "my_password")

    # Try to add it again
    with pytest.raises(KeychainError):
        keychain_access.add("my_account", "my_service", "my_password")
