from setuptools import setup

APP_NAME = "Notifyther"
APP = ['mainUI.py']
DATA_FILES = ['app.py', 'database.py', 'dialog.py', 'dialog.scpt', 'editReminder.py', 'notification.py']
OPTIONS = {
    'iconfile': 'icon.ico',
    'argv_emulation': True,
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': 'Notifyther',
        'CFBundleVersion': '1.9.0 Release',
        'CFBundleShortVersionString': '1.9.0',
        'NSHumanReadableCopyright': 'The program and all its files belong to https://github.com/sairex53'
    }
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
