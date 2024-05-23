from typing import Any

class NSData:
    def bytes(self) -> memoryview: ...

def SecItemAdd(query: dict[str, Any], none: None) -> int: ...
def SecItemCopyMatching(query: dict[str, Any], none: None) -> tuple[NSData | None, None]: ...
def SecItemDelete(query: dict[str, Any]) -> int: ...

kSecAttrService: str
kSecAttrAccount: str
kSecClass: str
kSecValueData: str
kSecClassGenericPassword: str
kSecMatchLimit: str
kSecReturnData: str
kSecMatchLimitOne: str
