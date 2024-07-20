#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf GitKraken-v%s.deb" % Version)
    shelltools.system("tar xvf data.tar.xz")
    shelltools.system("sed -i 's Icon=app Icon=gitkraken ' usr/share/applications/gitkraken.desktop")
def install():
    pisitools.insinto("/", "usr")
