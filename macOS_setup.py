"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['mousewalk.py']
APP_NAME = "Mousewalk"
DATA_FILES = []
OPTIONS = {
    'packages': 'pynput',
    'iconfile': 'icons/icon.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': 'Mouse can walk',
        'CFBundleIdentifier': 'com.catalyst.mousewalk',
        'CFBundleVersion': '1.0.1',
        'CFBundleShortVersionString': '1.0.0',
        'NSHumanReadableCopyright': u'Copyright © 2024, Catalyst',
        'LSUIElement': True,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)