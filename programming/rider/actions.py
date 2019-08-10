#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/rider", "JetBrains Rider-%s/*" % Version)
    pisitools.dosym("/opt/rider/bin/rider.sh", "/usr/bin/rider")