# XKCD URI OSX

An extremely simple OS X app which opens URIs that use the xkcd scheme in your default browser.

## Why?

The hell if I know. Some iOS apps started using it and it's seeped out a bit. This app just removes the annoyance when you encounter a link to them.


## Building

Requires Mac OS X.

`python setup.py py2app -s`

Note: Out of the box, [py2app is broken in El Capitan](https://forums.developer.apple.com/thread/6987). Upgrading py2app to the latest version fixes the issue.


## Using

There's nothing to do except have the app on your hard drive. When you click on a link that uses the xkcd scheme, it will simply open the comic in your web browser.

Try out some of these links:

* <a href="xkcd://353">Python</a>
* <a href="xkcd://327">Little Bobby Tables</a>
* <a href="xkcd://292/">GOTO</a> – Link has a traling slash.
* <a href="xkcd://303vwmjqkrcg">Compiling</a> - Link has extra gibberish to ignore.
