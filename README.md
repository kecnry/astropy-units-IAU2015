# astropy-units-IAU2015
light wrapper around astropy.units that changes constants and units to match those in the IAU 2015 resolution.

The [astropy](https://www.github.com/astropy/astropy) project has been working towards revising their units/constants system to be flexible to multiple sets of standards.  See the following issues and pull-requests for their discussion on the topic
* [Implement updated IAU B3 2015 constants if approved](https://github.com/astropy/astropy/issues/4026)
* [Organize constants into version modules](https://github.com/astropy/astropy/pull/6083)
* [Implement updated IAU B3 2015 constants](https://github.com/astropy/astropy/pull/4397)
* [astropy updated constants](https://github.com/astropy/astropy/pull/4956)

It [looks like](https://github.com/astropy/astropy/pull/6083) IAU 2015 resoultion constants/units will be available in astropy starting in version 2.0.0.  This module simply aims to provide the IAU set of standards, through astropy's units and constants infrastructure, for version before 2.0.0.  This is done by hacking and overriding the values within astropy.

This is currently only tested with python 2.7 and astropy 1.3.1.

## Dependencies

* [astropy](https://www.github.com/astropy/astropy)

## Installation

Installation is done using the standard python setup.py commands.

To install globally:

```
python setup.py build
sudo python setup.py install
```

Or to install locally:

```
python setup.py build
python setup.py install --user
```

## Basic Usage

```
from unitsiau2015 import u, c
print c.G.value
```

Note that once unitsiau2015 is imported, the values within the astropy package will change as well (for that python session).  See [simple.py example](https://github.com/kecnry/astropy-units-IAU2015/blob/master/examples/simple.py) to see this in action.

## Contributing

Contributions are welcome! Feel free to file an issue or fork and create a pull-request.
