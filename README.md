# a1pamfax

[Airport1]'s PamFax - short name **a1pamfax** - is a Python (3.6+) package that implements the [PamFax] API. 

It is an adaption of dynaptico's PamFax implementation - once written for Python 2 - adapted to work for Python 3.6 or later.
The old code has been kept whenever possible, on purpose. The behavior should be nearly the same.

For more information about the PamFax API that is used with this module, visit: [PamFax for Developers].

As this python module is still in development, please report any bugs or issues by raising an issue in this Github.

This module is for python 3.6+ and has only been tested against python 3.6+.
There is a chance it works for previous versions, however, too.

## Installation

You can install a1pamfax (soon) either via the Python Package Index (PyPI)
or from source.

To install using pip:

```
pip install a1pamfax
```

## Requirements

It is required to install at least (e.g. via ```pip install```):

* requests

## Tests

First (in test folder) 
copy the ```config.example.py``` to ```config.py``` and adapt the latter to your credentials. Then
run the test suite by:

```
cd test
python test.py
```
        
You may adapt the main method of ```test.py``` to en- or disable few tests. 

## Logging

This module uses the built-in Python logging.

## Documentation

There is no documentation for this package in Python 3 yet. But:
the documentation for the older Python 2 implementation by dynaptico is still available here:
[Dynaptico PamFax documentation (Python2)]
    
and nearly all methods and signatures have been kept ON PURPOSE, 
just adapted for Python 3. Only few private methods were changed.

## Thanks

To Dynaptico, on which this rewrite for Python 3 is heavily based on, see: [Dynaptico PamFax (Python2)].


[Airport1]: https://www.airport1.de/
[PamFax]: http://www.pamfax.biz/
[PamFax for Developers]: https://www.pamfax.biz/developers/introduction/
[Dynaptico PamFax documentation (Python2)]: http://packages.python.org/dynaptico-pamfax
[Dynaptico PamFax (Python2)]: https://github.com/dynaptico/pamfaxp