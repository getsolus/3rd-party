#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("tar xf android-studio-%s-linux.tar.gz" % get.srcVERSION())

def install():
    pisitools.insinto("/opt/android-studio", "android-studio/*")
    pisitools.dosym("/opt/android-studio/bin/studio.sh", "/usr/bin/android-studio")
