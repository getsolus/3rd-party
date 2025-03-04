#!/usr/bin/env python3

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    pisitools.insinto("/opt/pycharm-ce", "pycharm-community-%s/*" % Version)
    pisitools.dosym("/opt/pycharm-ce/bin/pycharm", "/usr/bin/pycharm-ce")
