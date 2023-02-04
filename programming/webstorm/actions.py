#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "223.8617.44"

def install():
    pisitools.insinto("/opt/webstorm", "WebStorm-%s/*" % Build)
    pisitools.dosym("/opt/webstorm/bin/webstorm.sh", "/usr/bin/webstorm")
