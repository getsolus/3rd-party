#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools
import shutil

def setup():
    shelltools.system("tar xf sublime_text_build_4113_x64.tar.xz")

def install():
    pisitools.insinto("/opt/sublime_text", "sublime_text/*")
    pisitools.dosym("/opt/sublime_text/sublime_text", "/usr/bin/sublime_text")
