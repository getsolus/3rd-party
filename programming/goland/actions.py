#!/usr/bin/env python3

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/goland", "GoLand-*/*")
    pisitools.dosym("/opt/goland/bin/goland", "/usr/bin/goland")