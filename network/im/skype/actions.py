#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf skypeforlinux_%s_amd64.deb" % Version)
    shelltools.system("tar xf data.tar.xz")
    shelltools.system("npm install -g asar")
    shelltools.system("asar extract usr/share/skypeforlinux/resources/app.asar new_app")
    shelltools.system(' ls -1 new_app/images/tray/linux | grep "@2x" | while read -r pngFile; do cp "new_app/images/tray/linux/$pngFile" "new_app/images/tray/linux/${pngFile//$@@2x/}"; done')
    shelltools.system("asar pack new_app app.asar")
    shelltools.system("cp app.asar usr/share/skypeforlinux/resources/app.asar")

def install():
    pisitools.insinto("/", "usr")
