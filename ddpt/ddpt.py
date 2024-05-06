#! /usr/bin/env python3

import os
import sys
import shutil
import numpy as np
import pandas as pd

from argparse import ArgumentParser, RawDescriptionHelpFormatter

import attachments
from package import Package

module_name = "ddpt"
module_version = "0.1.0rc"


def main():
	# Parse arguments
	parser = ArgumentParser(
		formatter_class = RawDescriptionHelpFormatter
	)
	parser.add_argument(
		"--version",
		action = "version",
		version = module_version,
		help = "Display version information and dependencies.",
	)
	parser.add_argument(
		"file",
		help = "Path to input directory."
	)
	args = parser.parse_args()

	out_dir = "output"

	# Check if path is valid
	if not os.path.isdir(args.file):
		# Check if path is a zip archive
		if args.file.endswith('.zip'):
			choice_zip = input("Zip file detected. Extract to a temporary directory? (y/n) ")
			if (choice_zip in ["Y", "y"]):
				shutil.unpack_archive(args.file, "temp")
				print("Extracted files to ./temp")
				print("Run ddpt again with the new path.")
		else:
			print("Invalid path: {}".format(args.file))
		quit()

	# Create dataframes
	ddp = Package()
	ddp.load(args.file)

	# Attachments
	attachments.get_list(ddp.messages, out_dir)
	attachments.download(ddp.messages, out_dir)
	#ddpt.attachments.plot_extension_stats(messages_df, out_dir)
	#del messages_df


if __name__ == '__main__':
	main()
