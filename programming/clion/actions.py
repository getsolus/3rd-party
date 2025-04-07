#!/usr/bin/env python3

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/clion", "clion-%s/*" % Version)
    pisitools.dosym("/opt/clion/bin/clion", "/usr/bin/clion")
