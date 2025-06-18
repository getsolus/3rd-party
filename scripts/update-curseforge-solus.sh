#!/bin/bash
# SETUP DIRECTORIES
sudo rm -rf ~/Downloads/curseforge-updater
mkdir -p ~/Downloads/curseforge-updater
cd ~/Downloads/curseforge-updater

# DOWNLOAD DEB AND EXTRACT VERSION
wget 'https://curseforge.overwolf.com/downloads/curseforge-latest-linux.deb' -O curseforge-latest-linux.deb
ar xf curseforge-latest-linux.deb
tar zxvf control.tar.gz ./control
VERSION=$(sed -n 2p control | grep -Po '(?<=Version: )\S+')

# RENAME DEB
mv curseforge-latest-linux.deb curseforge-$VERSION.deb

# COPY SCRIPT AND FILES
wget 'https://raw.githubusercontent.com/getsolus/packages/refs/heads/main/common/Scripts/ep-update.py' -O ep-update.py
wget 'https://raw.githubusercontent.com/msork/curseforge-solus/refs/heads/main/games/curseforge/actions.py' -O actions.py
wget 'https://raw.githubusercontent.com/msork/curseforge-solus/refs/heads/main/games/curseforge/pspec.xml' -O pspec.xml

# RUN SCRIPT
chmod +x ep-update.py
./ep-update.py $VERSION ./curseforge-$VERSION.deb

# BUILD AND INSTALL EOPKG
sudo eopkg bi --ignore-safety pspec.xml
sudo eopkg it -y ./*.eopkg

# REMOVE FILES
#sudo rm -rf ~/Downloads/curseforge-updater
#sudo rm ~/Downloads/curseforge-$SVER.x86_64.rpm
