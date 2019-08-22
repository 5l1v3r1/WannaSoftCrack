# uncompyle6 version 3.3.1
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: helpers.py
# Size of source mod 2**32: 5750 bytes
import sys, urllib.request, os, zipfile, win32com.client, requests

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def get_os_version():
    os_version = OSVERSIONINFOEXW()
    os_version.dwOSVersionInfoSize = sizeof(os_version)
    retcode = windll.Ntdll.RtlGetVersion(byref(os_version))
    if retcode != 0:
        return False
    else:
        return '%s.%s' % (str(os_version.dwMajorVersion.real), str(os_version.dwMinorVersion.real))


def checkurl(url):
    try:
        urllib.request.urlopen(url)
        return True
    except Exception as e:
        try:
            return False
        finally:
            e = None
            del e


def check_exists(file):
    if os.path.exists(file):
        return True
    else:
        return False


def lnktrgt(lnk):
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(lnk)
    return shortcut.Targetpath