#!/usr/bin/env python3

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/rider", "JetBrains Rider-%s/*" % Version)
    pisitools.dosym("/opt/rider/bin/rider", "/usr/bin/rider")