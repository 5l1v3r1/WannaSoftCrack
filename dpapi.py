# uncompyle6 version 3.3.1
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: dpapi.py
# Size of source mod 2**32: 5750 bytes
import os
from ctypes.wintypes import *
from ctypes import *
LPTSTR = LPSTR
LPCTSTR = LPSTR
PHANDLE = POINTER(HANDLE)
HANDLE = LPVOID
LPDWORD = POINTER(DWORD)
PVOID = c_void_p
INVALID_HANDLE_VALUE = c_void_p(-1).value
NTSTATUS = ULONG()
PWSTR = c_wchar_p
LPWSTR = c_wchar_p
PBYTE = POINTER(BYTE)
LPBYTE = POINTER(BYTE)
PSID = PVOID
LONG = c_long
WORD = c_uint16
CRYPTPROTECT_UI_FORBIDDEN = 1
CRED_TYPE_GENERIC = 1
CRED_TYPE_DOMAIN_VISIBLE_PASSWORD = 4
HKEY_CURRENT_USER = -2147483647
HKEY_LOCAL_MACHINE = -2147483646
KEY_READ = 131097
KEY_ENUMERATE_SUB_KEYS = 8
KEY_QUERY_VALUE = 1
ACCESS_READ = KEY_READ | KEY_ENUMERATE_SUB_KEYS | KEY_QUERY_VALUE
PROCESS_QUERY_INFORMATION = 1024
STANDARD_RIGHTS_REQUIRED = 983040
READ_CONTROL = 131072
STANDARD_RIGHTS_READ = READ_CONTROL
TOKEN_ASSIGN_PRIMARY = 1
TOKEN_DUPLICATE = 2
TOKEN_IMPERSONATE = 4
TOKEN_QUERY = 8
TOKEN_QUERY_SOURCE = 16
TOKEN_ADJUST_PRIVILEGES = 32
TOKEN_ADJUST_GROUPS = 64
TOKEN_ADJUST_DEFAULT = 128
TOKEN_ADJUST_SESSIONID = 256
TOKEN_READ = STANDARD_RIGHTS_READ | TOKEN_QUERY
tokenprivs = TOKEN_QUERY | TOKEN_READ | TOKEN_IMPERSONATE | TOKEN_QUERY_SOURCE | TOKEN_DUPLICATE | TOKEN_ASSIGN_PRIMARY | 131076
TOKEN_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED | TOKEN_ASSIGN_PRIMARY | TOKEN_DUPLICATE | TOKEN_IMPERSONATE | TOKEN_QUERY | TOKEN_QUERY_SOURCE | TOKEN_ADJUST_PRIVILEGES | TOKEN_ADJUST_GROUPS | TOKEN_ADJUST_DEFAULT | TOKEN_ADJUST_SESSIONID

class CREDENTIAL_ATTRIBUTE(Structure):
    _fields_ = [
     (
      'Keyword', LPSTR),
     (
      'Flags', DWORD),
     (
      'ValueSize', DWORD),
     (
      'Value', LPBYTE)]


PCREDENTIAL_ATTRIBUTE = POINTER(CREDENTIAL_ATTRIBUTE)

class CREDENTIAL(Structure):
    _fields_ = [
     (
      'Flags', DWORD),
     (
      'Type', DWORD),
     (
      'TargetName', LPSTR),
     (
      'Comment', LPSTR),
     (
      'LastWritten', FILETIME),
     (
      'CredentialBlobSize', DWORD),
     (
      'CredentialBlob', POINTER(c_char)),
     (
      'Persist', DWORD),
     (
      'AttributeCount', DWORD),
     (
      'Attributes', PCREDENTIAL_ATTRIBUTE),
     (
      'TargetAlias', LPSTR),
     (
      'UserName', LPSTR)]


PCREDENTIAL = POINTER(CREDENTIAL)

class DATA_BLOB(Structure):
    _fields_ = [
     (
      'cbData', DWORD),
     (
      'pbData', POINTER(c_char))]


class GUID(Structure):
    _fields_ = [
     (
      'data1', DWORD),
     (
      'data2', WORD),
     (
      'data3', WORD),
     (
      'data4', BYTE * 6)]


LPGUID = POINTER(GUID)

class VAULT_CREDENTIAL_ATTRIBUTEW(Structure):
    _fields_ = [
     (
      'keyword', LPWSTR),
     (
      'flags', DWORD),
     (
      'badAlign', DWORD),
     (
      'valueSize', DWORD),
     (
      'value', LPBYTE)]


PVAULT_CREDENTIAL_ATTRIBUTEW = POINTER(VAULT_CREDENTIAL_ATTRIBUTEW)

class VAULT_BYTE_BUFFER(Structure):
    _fields_ = [
     (
      'length', DWORD),
     (
      'value', PBYTE)]


class DATA(Structure):
    _fields_ = [
     (
      'guid', GUID),
     (
      'string', LPWSTR),
     (
      'byteArray', VAULT_BYTE_BUFFER),
     (
      'protectedArray', VAULT_BYTE_BUFFER),
     (
      'attribute', PVAULT_CREDENTIAL_ATTRIBUTEW),
     (
      'sid', DWORD)]


class Flag(Structure):
    _fields_ = [
     (
      '0x00', DWORD),
     (
      '0x01', DWORD),
     (
      '0x02', DWORD),
     (
      '0x03', DWORD),
     (
      '0x04', DWORD),
     (
      '0x05', DWORD),
     (
      '0x06', DWORD),
     (
      '0x07', DWORD),
     (
      '0x08', DWORD),
     (
      '0x09', DWORD),
     (
      '0x0a', DWORD),
     (
      '0x0b', DWORD),
     (
      '0x0c', DWORD),
     (
      '0x0d', DWORD)]


class VAULT_ITEM_DATA(Structure):
    _fields_ = [
     (
      'data', DATA)]


PVAULT_ITEM_DATA = POINTER(VAULT_ITEM_DATA)

class VAULT_ITEM_WIN8(Structure):
    _fields_ = [
     (
      'id', GUID),
     (
      'pName', PWSTR),
     (
      'pResource', PVAULT_ITEM_DATA),
     (
      'pUsername', PVAULT_ITEM_DATA),
     (
      'pPassword', PVAULT_ITEM_DATA),
     (
      'unknown0', PVAULT_ITEM_DATA),
     (
      'LastWritten', FILETIME),
     (
      'Flags', DWORD),
     (
      'cbProperties', DWORD),
     (
      'Properties', PVAULT_ITEM_DATA)]


PVAULT_ITEM_WIN8 = POINTER(VAULT_ITEM_WIN8)

class OSVERSIONINFOEXW(Structure):
    _fields_ = [
     (
      'dwOSVersionInfoSize', c_ulong),
     (
      'dwMajorVersion', c_ulong),
     (
      'dwMinorVersion', c_ulong),
     (
      'dwBuildNumber', c_ulong),
     (
      'dwPlatformId', c_ulong),
     (
      'szCSDVersion', c_wchar * 128),
     (
      'wServicePackMajor', c_ushort),
     (
      'wServicePackMinor', c_ushort),
     (
      'wSuiteMask', c_ushort),
     (
      'wProductType', c_byte),
     (
      'wReserved', c_byte)]


class CRYPTPROTECT_PROMPTSTRUCT(Structure):
    _fields_ = [
     (
      'cbSize', DWORD),
     (
      'dwPromptFlags', DWORD),
     (
      'hwndApp', HWND),
     (
      'szPrompt', LPCWSTR)]


PCRYPTPROTECT_PROMPTSTRUCT = POINTER(CRYPTPROTECT_PROMPTSTRUCT)

class LUID(Structure):
    _fields_ = [
     (
      'LowPart', DWORD),
     (
      'HighPart', LONG)]


PLUID = POINTER(LUID)

class SID_AND_ATTRIBUTES(Structure):
    _fields_ = [
     (
      'Sid', PSID),
     (
      'Attributes', DWORD)]


class TOKEN_USER(Structure):
    _fields_ = [
     (
      'User', SID_AND_ATTRIBUTES)]


class LUID_AND_ATTRIBUTES(Structure):
    _fields_ = [
     (
      'Luid', LUID),
     (
      'Attributes', DWORD)]


class TOKEN_PRIVILEGES(Structure):
    _fields_ = [
     (
      'PrivilegeCount', DWORD),
     (
      'Privileges', LUID_AND_ATTRIBUTES)]


PTOKEN_PRIVILEGES = POINTER(TOKEN_PRIVILEGES)

class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
     (
      'nLength', DWORD),
     (
      'lpSecurityDescriptor', LPVOID),
     (
      'bInheritHandle', BOOL)]


PSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)
advapi32 = WinDLL('advapi32', use_last_error=True)
crypt32 = WinDLL('crypt32', use_last_error=True)
kernel32 = WinDLL('kernel32', use_last_error=True)
RevertToSelf = advapi32.RevertToSelf
RevertToSelf.restype = BOOL
RevertToSelf.argtypes = []
ImpersonateLoggedOnUser = advapi32.ImpersonateLoggedOnUser
ImpersonateLoggedOnUser.restype = BOOL
ImpersonateLoggedOnUser.argtypes = [HANDLE]
DuplicateTokenEx = advapi32.DuplicateTokenEx
DuplicateTokenEx.restype = BOOL
DuplicateTokenEx.argtypes = [HANDLE, DWORD, PSECURITY_ATTRIBUTES, DWORD, DWORD, POINTER(HANDLE)]
AdjustTokenPrivileges = advapi32.AdjustTokenPrivileges
AdjustTokenPrivileges.restype = BOOL
AdjustTokenPrivileges.argtypes = [HANDLE, BOOL, PTOKEN_PRIVILEGES, DWORD, PTOKEN_PRIVILEGES, POINTER(DWORD)]
LookupPrivilegeValueA = advapi32.LookupPrivilegeValueA
LookupPrivilegeValueA.restype = BOOL
LookupPrivilegeValueA.argtypes = [LPCTSTR, LPCTSTR, PLUID]
ConvertSidToStringSidA = advapi32.ConvertSidToStringSidA
ConvertSidToStringSidA.restype = BOOL
ConvertSidToStringSidA.argtypes = [DWORD, POINTER(LPTSTR)]
LocalAlloc = kernel32.LocalAlloc
LocalAlloc.restype = HANDLE
LocalAlloc.argtypes = [PSID, DWORD]
GetTokenInformation = advapi32.GetTokenInformation
GetTokenInformation.restype = BOOL
GetTokenInformation.argtypes = [HANDLE, DWORD, LPVOID, DWORD, POINTER(DWORD)]
OpenProcess = kernel32.OpenProcess
OpenProcess.restype = HANDLE
OpenProcess.argtypes = [DWORD, BOOL, DWORD]
OpenProcessToken = advapi32.OpenProcessToken
OpenProcessToken.restype = BOOL
OpenProcessToken.argtypes = [HANDLE, DWORD, POINTER(HANDLE)]
CloseHandle = kernel32.CloseHandle
CloseHandle.restype = BOOL
CloseHandle.argtypes = [HANDLE]
CredEnumerate = advapi32.CredEnumerateA
CredEnumerate.restype = BOOL
CredEnumerate.argtypes = [LPCTSTR, DWORD, POINTER(DWORD), POINTER(POINTER(PCREDENTIAL))]
CredFree = advapi32.CredFree
CredFree.restype = PVOID
CredFree.argtypes = [PVOID]
memcpy = cdll.msvcrt.memcpy
memcpy.restype = PVOID
memcpy.argtypes = [PVOID]
LocalFree = kernel32.LocalFree
LocalFree.restype = HANDLE
LocalFree.argtypes = [HANDLE]
CryptUnprotectData = crypt32.CryptUnprotectData
CryptUnprotectData.restype = BOOL
CryptUnprotectData.argtypes = [POINTER(DATA_BLOB), POINTER(LPWSTR), POINTER(DATA_BLOB), PVOID, PCRYPTPROTECT_PROMPTSTRUCT, DWORD, POINTER(DATA_BLOB)]
try:
    prototype = WINFUNCTYPE(ULONG, DWORD, LPDWORD, POINTER(LPGUID))
    vaultEnumerateVaults = prototype(('VaultEnumerateVaults', windll.vaultcli))
    prototype = WINFUNCTYPE(ULONG, LPGUID, DWORD, HANDLE)
    vaultOpenVault = prototype(('VaultOpenVault', windll.vaultcli))
    prototype = WINFUNCTYPE(ULONG, HANDLE, DWORD, LPDWORD, POINTER(c_char_p))
    vaultEnumerateItems = prototype(('VaultEnumerateItems', windll.vaultcli))
    prototype = WINFUNCTYPE(ULONG, HANDLE, LPGUID, PVAULT_ITEM_DATA, PVAULT_ITEM_DATA, PVAULT_ITEM_DATA, HWND, DWORD, POINTER(PVAULT_ITEM_WIN8))
    vaultGetItem8 = prototype(('VaultGetItem', windll.vaultcli))
    prototype = WINFUNCTYPE(ULONG, LPVOID)
    vaultFree = prototype(('VaultFree', windll.vaultcli))
    prototype = WINFUNCTYPE(ULONG, PHANDLE)
    vaultCloseVault = prototype(('VaultCloseVault', windll.vaultcli))
except:
    pass

def getData(blobOut):
    cbData = int(blobOut.cbData)
    pbData = blobOut.pbData
    buffer = c_buffer(cbData)
    memcpy(buffer, pbData, cbData)
    LocalFree(pbData)
    return buffer.raw


def isx64machine():
    archi = os.environ.get('PROCESSOR_ARCHITEW6432', '')
    if '64' in archi:
        return True
    else:
        archi = os.environ.get('PROCESSOR_ARCHITECTURE', '')
        if '64' in archi:
            return True
        return False


isx64 = isx64machine()

def OpenKey(key, path, index=0, access=KEY_READ):
    if isx64:
        return winreg.OpenKey(key, path, index, access | winreg.KEY_WOW64_64KEY)
    else:
        return winreg.OpenKey(key, path, index, access)


def Win32CryptUnprotectData(cipherText, entropy=None):
    bufferIn = c_buffer(cipherText, len(cipherText))
    blobIn = DATA_BLOB(len(cipherText), bufferIn)
    blobOut = DATA_BLOB()
    if entropy:
        bufferEntropy = c_buffer(entropy, len(entropy))
        blobEntropy = DATA_BLOB(len(entropy), bufferEntropy)
        if CryptUnprotectData(byref(blobIn), None, byref(blobEntropy), None, None, 0, byref(blobOut)):
            return getData(blobOut)
        return False
    else:
        if CryptUnprotectData(byref(blobIn), None, None, None, None, 0, byref(blobOut)):
            return getData(blobOut)
        return False