"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['ctfevalgui.py']
DATA_FILES = ['images/ctfeval_logo.png', ]
PACKAGES = ['py2app','numpy','PIL','scipy','matplotlib']
OPTIONS = {
  'argv_emulation': True, 
  'iconfile': 'images/ctfeval_logo.icns', 
  'plist': {'CFBundleShortVersionString':'0.1.0',},
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=PACKAGES,
)