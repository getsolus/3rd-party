#!/usr/bin/env python3

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "253.29346.242"

def install():
    pisitools.insinto("/opt/webstorm", "WebStorm-%s/*" % Build)
    pisitools.dosym("/opt/webstorm/bin/webstorm", "/usr/bin/webstorm")
