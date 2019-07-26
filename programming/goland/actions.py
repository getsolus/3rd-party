#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/goland", "GoLand-*/*")
    pisitools.dosym("/opt/goland/bin/goland.sh", "/usr/bin/goland")