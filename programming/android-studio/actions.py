#!/usr/bin/env python3

from pisi.actionsapi import get, pisitools

def install():
    pisitools.insinto("/opt/android-studio", "*")
    pisitools.dosym("/opt/android-studio/bin/studio.sh", "/usr/bin/android-studio")
