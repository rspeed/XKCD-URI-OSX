from setuptools import setup

setup(
	app = ['xkcd.py'],
	options = {
		'py2app': {
			'argv_emulation': True,
			'plist': {
				'CFBundleIdentifier': 'rocks.robspeed.xkcd',
				'CFBundleName': 'XKCD',
				'CFBundleShortVersionString': '1.0',
				'CFBundleURLTypes': [
					{
						'CFBundleURLName': 'XKCD helper',
						'CFBundleURLSchemes': [
							'xkcd'
						]
					}
				],
				'LSBackgroundOnly': True
			}
		}
	},
	setup_requires = ['py2app'],
)
