#!/usr/bin/env python3

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "241.17011.90"

def install():
    pisitools.insinto("/opt/webstorm", "WebStorm-%s/*" % Build)
    pisitools.dosym("/opt/webstorm/bin/webstorm.sh", "/usr/bin/webstorm")
