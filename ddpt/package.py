import os

import pandas as pd


class Package:
	def __init__(self):
		self.messages = None

	def load(self, path: str):
		messages_json = []
		for subdir, dirs, files in os.walk(os.path.join(path, "messages")):
			for file in files:
				filepath = os.path.join(subdir, file)
				if file.endswith('messages.json'):
					# print(filepath)
					msg = pd.read_json(filepath)
					messages_json.append(msg)
		self.messages = pd.concat(messages_json, axis=0, ignore_index=True)
		del messages_json
