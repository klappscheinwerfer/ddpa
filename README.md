# Discord Data Package Tools

A tool for analysing and extracting data from a Discord data package.

Currently work-in-progress

## Features

- Create a list of all attachments
- Download all attachments

## Usage

- Clone this repository `git clone https://github.com/klappscheinwerfer/discord-data-viewer`
- Create a virtual environment `python3 -m venv virtual-environment-name`
- Activate the virtual environment `source ./venv/bin/activate`
- Install all dependencies `pip install -r requirements.txt`
- Create directories `mkdir ./output` `mkdir ./output/attachments`
- Run ddpt.py with a path to your zip file or extracted folder `python3 ddpt.py path/to/data/`
