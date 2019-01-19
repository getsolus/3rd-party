#!/usr/bin/python
from pisi.actionsapi import get, pisitools

WorkDir = "."
Version = get.srcVERSION()


def install():
    pisitools.insinto("/opt/postman", "Postman/*")
    pisitools.dosym("/opt/postman/Postman", "/usr/bin/postman")
