#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("tar xf android-studio-ide-193.6626763-linux.tar.gz")

def install():
    pisitools.insinto("/opt/android-studio", "android-studio/*")
    pisitools.dosym("/opt/android-studio/bin/studio.sh", "/usr/bin/android-studio")
