Third Party Apps (DEPRECATED)
=============================

**Note**: This repo will not accept NEW packages as we are replacing the majority of them in Solus with a modern solution like flatpak. After we have flatpak integrated in the Software Center we will begin forceful deprecation of this repository.

This repo contains the build files required to create packages that cannot be redistributed, whether for licensing restrictions or otherwise.

For more information about 3rd party applications in Solus, visit our Help Center page at https://getsol.us/articles/software/third-party/en/.

## Updating and building a package

A script to update the `pspec.xml` for a Third Party App is included in our ["common" repository](https://dev.getsol.us/source/common/) under `/common/Scripts/ep-update.py`

To update an app to a new version you can use the following command
```
ep-update.py <version> <url-to-new-deb/zip/etc>
```
e.g.
```
ep-update.py 9.5.0 https://release.gitkraken.com/linux/gitkraken-amd64.deb
```
After that you can build the package with
```
sudo eopkg bi --ignore-safety pspec.xml
```
This will create an `.eopkg` package that you can install and test

DO NOT PUSH THESE BINARY PACKAGES, only the changes to `pspec.xml` (and if necessary `actions.py`).
The git history has been reset because it ballooned to nearly 300MB in size. :)
