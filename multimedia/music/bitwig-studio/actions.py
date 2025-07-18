#!/usr/bin/env python3

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf bitwig-studio-%s.deb" % Version)
    shelltools.system("tar xf data.tar.zst")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
