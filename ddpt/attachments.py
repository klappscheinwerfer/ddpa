import collections
import os
import requests
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from tqdm import tqdm


def get_list(df, out):
	if os.path.isfile(out + "/links.txt"):
		print("File already exists: " + out + "links.txt")
	else:
		np.savetxt(out + "/links.txt", df["Attachments"].replace("", np.nan).dropna().to_numpy() , fmt='%s')


def download(df, out):
	print("Downloading attachments")
	out = out + "/attachments"
	# Multiple attachments possible?
	for url in tqdm(df["Attachments"].replace("", np.nan).dropna()):
		spliturl = url.split("/")
		fname = spliturl[-2] + "_" + spliturl[-1].split("?")[0]
		# print(fname)
		if os.path.isfile(out + "/" + fname):
			pass
			# print("File already exists: " + out + fname)
		else:
			response = requests.get(url)
			open(out + "/" + fname, "wb").write(response.content)
			#print("Download finished: " + fname)


def plot_extension_stats(df, out):
	extensions = []
	for url in df["Attachments"].replace("", np.nan).dropna():
		extensions.append(os.path.splitext(url)[1])
	c = collections.Counter(extensions)
	plt.pie(c.values(), labels = c.keys())
	plt.show()
