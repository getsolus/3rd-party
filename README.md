Third Party Apps (DEPRECATED)
=============================

**Note**: This repo will not accept NEW packages as we are replacing the majority of them in Solus with a modern solution like flatpak.

This repo contains the build files required to create packages that cannot be redistributed, whether for licensing restrictions or otherwise.

For more information about 3rd party applications in Solus, visit our Help Center page at https://help.getsol.us/docs/user/software/third-party/.

## Updating and building a package

A script to update the `pspec.xml` for a Third Party App is included in the `common` folder of our ["packages" repository](https://github.com/getsolus/packages) under `/common/Scripts/ep-update.py`

To update an app to a new version you can use the following command
```
ep-update.py <version> <url-to-new-deb/zip/etc>
```
e.g.
```
ep-update.py 9.5.0 https://release.gitkraken.com/linux/gitkraken-amd64.deb
```
To build your package install `python-eopkg` and use the following command
```
sudo eopkg.py3 bi --ignore-safety pspec.xml
```

This will create an `.eopkg` package that you can install and test

DO NOT PUSH THESE BINARY PACKAGES, only the changes to `pspec.xml` (and if necessary `actions.py`).
The git history has been reset because it ballooned to nearly 300MB in size. :)
