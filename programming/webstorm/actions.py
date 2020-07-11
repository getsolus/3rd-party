#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "201.8538.32"

def install():
    pisitools.insinto("/opt/webstorm", "WebStorm-%s/*" % Build)
    pisitools.dosym("/opt/webstorm/bin/webstorm.sh", "/usr/bin/webstorm")
