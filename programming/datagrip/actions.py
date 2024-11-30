#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/datagrip", "DataGrip-%s/*" % Version)
    pisitools.dosym("/opt/datagrip/bin/datagrip", "/usr/bin/datagrip")
