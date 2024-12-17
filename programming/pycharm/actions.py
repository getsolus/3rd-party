#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/pycharm", "pycharm-%s/*" % Version)
    pisitools.dosym("/opt/pycharm/bin/pycharm", "/usr/bin/pycharm")
