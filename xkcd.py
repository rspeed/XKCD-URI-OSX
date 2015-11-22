import sys, re, webbrowser, logging
from logging.handlers import SysLogHandler


# Set up logging for OS X
syslog = SysLogHandler(address="/var/run/syslog")
log = logging.getLogger()
log.addHandler(syslog)

try:
	xkcd_uri = sys.argv[1]
except IndexError:
	# Only one thing to do now
	import antigravity
	sys.exit(0)

try:
	strip_num = re.findall("xkcd://+(\d+)", xkcd_uri, re.I).pop()
except IndexError:
	log.error("Didn't get a valid xkcd URI")
	sys.exit(1)

log.debug("Opened XKCD strip #%s" % strip_num)
webbrowser.open("http://xkcd.com/%s/" % strip_num)
sys.exit(0)
