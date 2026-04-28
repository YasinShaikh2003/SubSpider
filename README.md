# SubSpider

SubSpider is a CLI-based passive subdomain discovery tool that finds subdomains and resolves their IP addresses using OSINT sources.

## Features

* Passive subdomain discovery
* DNS resolution with IP output
* CLI-based interface
* Lightweight and fast

## Installation

git clone https://github.com/YasinShaikh2003/SubSpider.git

cd SubSpider 

python3 -m venv sub

source sub/bin/activate

pip install -r requirements.txt

pip install .

## Usage

python subspider.py -d example.com

Save output

python subspider.py -d example.com -o results.txt

## Disclaimer

This tool is intended for educational and authorized security testing only.
