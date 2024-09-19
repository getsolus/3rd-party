#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr", "/opt"],
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf ocenaudio_ubuntu24.04.deb")
    shelltools.system("tar xf data.tar.zst")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
