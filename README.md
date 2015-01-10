# py-spotternetwork
A python module to convert kml positions on [spotternetwork](http://www.spotternetwork.org/) to geojson.

## Installation
This has been tested on ubuntu 14.04 and Fedora 18.

### Operating system package dependencies for Ubuntu 14.04
- build-essential
- python-dev
- python-pip
- python-setuptools
- libxslt1-dev
- libz-dev

### Operating system package dependencies for Fedora 18
- python-setuptools
- libxslt-devel
- libxml2-devel
- python-devel

### Installing with setuptools
To install with setup tools clone the repository and run the following:

```
python setup.py install
```

## Usage
Get positions in geojson format
```python
from spotternetowrk import SpotterNetwork
spotters = SpotterNetwork()
spotters.load_from_kml()
positions = spotters.positions
```
You can also just run it from the command line.  In the future I may get around to using consolescripts to make an actual cli.
```sh.command
python -mspotternetwork
```
