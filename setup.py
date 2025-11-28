from setuptools import setup

APP = ['timer.py']
OPTIONS = {
    'argv_emulation': False,
    'plist': {
        'CFBundleName': 'Daily Timer',
        'CFBundleDisplayName': 'Daily Timer',
        'CFBundleIdentifier': 'com.dailytimer.app',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement': False,
    },
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
