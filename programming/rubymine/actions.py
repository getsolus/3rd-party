#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()
MainRelease = ".".join(Version.split(".")[0:2])

def install():
    pisitools.insinto("/opt/rubymine", "RubyMine-%s/*" % Version)
    pisitools.dosym("/opt/rubymine/bin/rubymine", "/usr/bin/rubymine")