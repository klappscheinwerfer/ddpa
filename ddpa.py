import json
import sys
import shutil
import matplotlib as mpl
from os import path

from ddpa import get_all_images


if __name__ == '__main__':
	# Get path to data
	if len(sys.argv) < 2:
		print("No path provided")
		quit()
	data_path = sys.argv[1]
	if path.isfile(data_path):
		shutil.unpack_archive(data_path, "temp/")
		datapath = "temp/"
	elif (path.isdir(data_path)):
		pass
	else:
		print("Invalid path: {}".format(data_path))
		quit()
	
	get_all_images.get_all_images()