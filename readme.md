# XKCD URI OSX

An extremely simple OS X app which opens URIs that use the xkcd scheme in your default browser.

## Download

Instructions are available [here](//rspeed.github.io/XKCD-URI-OSX/).


## Build

Requires Mac OS X.

`python setup.py py2app -s`

Note: Out of the box, [py2app is broken in El Capitan](https://forums.developer.apple.com/thread/6987). Upgrading py2app to the latest version fixes the issue.
