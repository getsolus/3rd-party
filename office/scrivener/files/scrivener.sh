#! /bin/sh

makeAbsolute() {
    case $1 in
        /*)
            # already absolute, return it
            echo "$1"
            ;;
        *)
            # relative, prepend $2 made absolute
            echo `makeAbsolute "$2" "$PWD"`/"$1" | sed 's,/\.$,,'
            ;;
    esac
}

me=`which "$0"` # Search $PATH if necessary
if test -L "$me"; then
    # Try readlink(1)
    readlink=`type readlink 2>/dev/null` || readlink=
    if test -n "$readlink"; then
        # We have readlink(1), so we can use it. Assuming GNU readlink (for -f).
        me=`readlink -nf "$me"`
    else
        # No readlink(1), so let's try ls -l
        me=`ls -l "$me" | sed 's/^.*-> //'`
        base=`dirname "$me"`
        me=`makeAbsolute "$me" "$base"`
    fi
fi

bindir=`dirname "$me"`
libdir=`cd "$bindir/../lib" ; pwd`
LD_LIBRARY_PATH=$libdir
export LD_LIBRARY_PATH
unset QT_PLUGIN_PATH
#export QT_DEBUG_PLUGINS=1  
export LD_PRELOAD=/usr/lib64/libfreetype.so.6
exec "$bindir/Scrivener" ${1+"$@"}
