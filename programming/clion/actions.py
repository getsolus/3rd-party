#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/clion", "clion-%s/*" % Version)
    pisitools.dosym("/opt/clion/bin/clion.sh", "/usr/bin/clion")
