import ddpa
import os
import sys
import shutil
import numpy as np
import pandas as pd


if __name__ == '__main__':
	# Get path to data
	if len(sys.argv) < 2:
		print("No path provided")
		quit()
	in_dir = sys.argv[1]
	if os.path.isfile(in_dir):
		shutil.unpack_archive(in_dir, "temp/")
		in_dir = "temp/"
	elif (os.path.isdir(in_dir)):
		pass
	else:
		print("Invalid path: {}".format(in_dir))
		quit()
	out_dir = "output/"

	# Create dataframes
	# Messages
	messages_csv = []
	for subdir, dirs, files in os.walk(in_dir + "messages"):
		for file in files:
			filepath = os.path.join(subdir, file)
			if file.endswith('.csv'):
				msg = pd.read_csv(filepath)
				messages_csv.append(msg)
	messages_df = pd.concat(messages_csv, axis=0, ignore_index=True)
	del messages_csv

	# Attachments
	ddpa.attachments.get_list(messages_df, out_dir)
	ddpa.attachments.download(messages_df, out_dir)