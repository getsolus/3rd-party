#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools


NoStrip = ["/"]
KeepSpecial=["python"]
IgnoreAutodep = True


def setup():
    shelltools.system("ar xf SpiderOakONE_*.deb")
    shelltools.system("tar xf data.tar.xz")
    shelltools.system("rm -r etc/apt")
    shelltools.system("rm -r etc/xdg")


def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
