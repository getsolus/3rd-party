#!/usr/bin/env python3

# Created For Solus Operating System

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/opt/sublime_text", "*")
    pisitools.domove("/opt/sublime_text/sublime_text.desktop", "/usr/share/applications")
    pisitools.domove("/opt/sublime_text/Icon/*", "/usr/share/icons/hicolor/")
    pisitools.dosym("/opt/sublime_text/sublime_text", "/usr/bin/sublime_text")
    pisitools.dosym("/opt/sublime_text/sublime_text", "/usr/bin/subl")
