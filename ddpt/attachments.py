import collections
import os
import requests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def get_list(df, out):
	if os.path.isfile(out + "links.txt"):
		print("File already exists: " + out + "links.txt")
	else:
		np.savetxt(out + "links.txt", df["Attachments"].dropna().to_numpy() , fmt='%s')


def download(df, out):
	out = out + "attachments/"
	# Multiple attachments possible?
	for url in df["Attachments"].dropna():
		spliturl = url.split("/")
		fname = spliturl[-2] + "_" + spliturl[-1]
		if os.path.isfile(out + fname):
			print("File already exists: " + out + fname)
		else:
			response = requests.get(url)
			open(out + fname, "wb").write(response.content)
			print("Download finished: " + url)


def plot_extension_stats(df, out):
	extensions = []
	for url in df["Attachments"].dropna():
		extensions.append(os.path.splitext(url)[1])
	c = collections.Counter(extensions)
	plt.pie(c.values(), labels = c.keys())
	plt.show()