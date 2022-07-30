#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "222.3345.108"

def install():
    pisitools.insinto("/opt/webstorm", "WebStorm-%s/*" % Build)
    pisitools.dosym("/opt/webstorm/bin/webstorm.sh", "/usr/bin/webstorm")
