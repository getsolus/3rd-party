#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf curseforge-%s.deb" % Version)
    shelltools.system("tar xf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
    pisitools.dosym("/opt/CurseForge/curseforge", "/usr/bin/curseforge")