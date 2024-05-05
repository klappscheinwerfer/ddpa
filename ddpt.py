import ddpt
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
		shutil.unpack_archive(in_dir, "temp")
		in_dir = "temp"
	elif (os.path.isdir(in_dir)):
		pass
	else:
		print("Invalid path: {}".format(in_dir))
		quit()
	out_dir = "output"

	# Create dataframes
	# Messages
	messages_json = []
	for subdir, dirs, files in os.walk(in_dir + "/messages"):
		for file in files:
			filepath = os.path.join(subdir, file)
			if file.endswith('messages.json'):
				# print(filepath)
				msg = pd.read_json(filepath)
				messages_json.append(msg)
	messages_df = pd.concat(messages_json, axis=0, ignore_index=True)
	del messages_json

	"""Activity
	#activities_json = []
	for subdir, dirs, files in os.walk(in_dir + "activity"):
		for file in files:
			try:
				filepath = os.path.join(subdir, file)
				print(filepath)
				events = pd.read_json(filepath, lines=True)
				print(events)
				del events
			except:
				print("exception")
			#activities_json.append(events)"""

	# Attachments
	ddpt.attachments.get_list(messages_df, out_dir)
	ddpt.attachments.download(messages_df, out_dir)
	#ddpt.attachments.plot_extension_stats(messages_df, out_dir)
	#del messages_df
