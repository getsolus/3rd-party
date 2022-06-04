#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "221.5787.33"

def install():
    pisitools.insinto("/opt/phpstorm", "PhpStorm-%s/*" % Build)
    pisitools.dosym("/opt/phpstorm/bin/phpstorm.sh", "/usr/bin/phpstorm")
