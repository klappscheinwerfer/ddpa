# Copyright (C) 2022 Toms Grants
# MIT license - see LICENSE for more information

import sys
import zipfile
import json

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QLabel

def window():
   app = QtGui.QGuiApplication(sys.argv)

# Check arguments
if len(sys.argv) < 2:
	print("No path provided")
	quit()

archive = zipfile.ZipFile(sys.argv[1], 'r')
file = archive.open('README.txt')

# TO-DO: Go trough
# - account
# - activity
# - messages
# - programs
# - servers

# Output
f = open("output/a.txt", "a")

# Account
with archive.open("account/user.json") as account_user:
	account_user_data = json.load(account_user)
	f.write(json.dumps(account_user_data, indent=4, sort_keys=True))

# Close file
f.close()

if __name__ == '__main__':
   window()
