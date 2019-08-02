#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/rubymine", "RubyMine-%s/*" % Version)
    pisitools.dosym("/opt/rubymine/bin/rubymine.sh", "/usr/bin/rubymine")