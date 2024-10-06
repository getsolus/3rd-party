#!/usr/bin/env python3

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr", "/opt"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf RoundPie-%s_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
