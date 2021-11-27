# Spider Demo
![Python Version](https://img.shields.io/badge/Python-3.8-green.svg)

Simple Spider demo to retrieve phrases data with Scrapy.

## Requirements

- python3
- pip3
- virtualenv (recommended)

## Setup

```bash
# install and activate virtual environment
virtualenv venv --python=python3
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# run the spider
scrapy crawl phrases
```

The scraped data will be stored in a `phrases.txt` file.
