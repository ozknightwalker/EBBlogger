from __future__ import unicode_literals

import os

if os.path.isfile('build.zip'):
    os.remove('build.zip')

os.system('zip build.zip -r * .[^.]* -x venv\* .git\* *.pyc *.sqlite3')
