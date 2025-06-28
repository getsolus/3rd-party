#!/usr/bin/env python3

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "251.26927.60"

def install():
    pisitools.insinto("/opt/phpstorm", "PhpStorm-%s/*" % Build)
    pisitools.dosym("/opt/phpstorm/bin/phpstorm", "/usr/bin/phpstorm")
