#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "243.21565.202"

def install():
    pisitools.insinto("/opt/phpstorm", "PhpStorm-%s/*" % Build)
    pisitools.dosym("/opt/phpstorm/bin/phpstorm.sh", "/usr/bin/phpstorm")
