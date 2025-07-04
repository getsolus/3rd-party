#!/usr/bin/env python3

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

Version = get.srcVERSION()
WorkDir = "."
IgnoreAutodep = True

def build():
    shelltools.system("pwd")
    shelltools.system("ar xf teamviewer_%s_amd64.deb" % Version)
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.insinto("/usr/", "./usr/*")
    pisitools.insinto("/etc/systemd/system", "./opt/teamviewer/tv_bin/script/teamviewerd.service")

    # Remove outaded/incompatible qt libs
    pisitools.removeDir("/opt/teamviewer/tv_bin/RTlib/qt/lib")

    #necessary symlinks
    pisitools.dosym("/etc/systemd/system/teamviewerd.service", "/etc/systemd/system/multi-user.target.wants/teamviewerd.service")
    pisitools.dosym("/opt/teamviewer/tv_bin/desktop/teamviewer_256.png", "/usr/share/pixmaps/teamviewer.png")

    pisitools.dodir("/etc/teamviewer")

    shelltools.chmod("%s/opt/teamviewer/doc/*" % get.installDIR(),0o0755)
    shelltools.chmod("%s/opt/teamviewer/tv_bin/*" % get.installDIR(),0o0755)
