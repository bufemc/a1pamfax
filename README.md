# a1pamfax

[Airport1]'s PamFax - short name **a1pamfax** - is a Python (3.6+) package that implements the [PamFax] API. 

It is an adaption of [Dynaptico PamFax (Python2)] - once written for Python 2 - adapted to work for Python 3.6 or later.
The old code has been kept whenever possible, on purpose. The behavior should be nearly the same.

For more information about the PamFax API, visit: [PamFax for Developers].

As this package is still in development, please report any bugs or issues by raising an issue in this Github.

This module is for Python 3.6+ and has only been tested against Python 3.6+.
There is a big chance it works for previous versions, however, too.

### Installation

You can install ```a1pamfax``` either via the Python Package Index (PyPI)
or from source.

To install using pip:

```
pip install a1pamfax
```

This is my first public package following the instructions on [Python-Packaging]. 
So far I included the test, test data (a pdf file), a config example and an example in it, not sure if that's too much? 

### Requirements

It is required to install at least (e.g. via ```pip install```):

* requests

### Tests

First copy the file ```config.example.py``` and rename it to ```config.py``` and adapt it to your credentials. Then
run the test suite by:

```
cd test
python test.py
```
        
You may adapt the main method of ```test.py``` to en- or disable few tests. 

### Usage

There is also an example.py provided, but in short:

```
from config import HOST, USERNAME, PASSWORD, APIKEY, APISECRET
from pamfax import PamFax

pamfax = PamFax(USERNAME, PASSWORD, host=HOST, apikey=APIKEY, apisecret=APISECRET)
response = pamfax.get_current_settings()
print(response)
```

### Documentation

There is no documentation for this package in Python 3 yet. But:
the documentation for the older Python 2 implementation by dynaptico is still available here:
[Dynaptico PamFax documentation (Python2)]
    
and nearly all methods and signatures have been kept ON PURPOSE, 
just adapted for Python 3. Only few private methods were changed.

See also section Particularities.

### Integrity

All methods in the PamFax API should be implemented by this package, except:

* Dropbox methods

Those have changed since then quite heavily, and still have to be adapted.

### Particularities

As said, the code is heavily based on an old package for Python 2. It was just adapted to run "the same" on Python 3.
Intentionally nearly all methods and signatures have been kept, except the implementation might be different sometimes.
So the code has only been touched where it was required, e.g. it's using now ```requests```'s session.
I tried to stick to the coding style of dynaptico.
However, few private methods had to be changed in their signature:

* _get_and_check_response
* _get
* _post   

### Thanks

To Dynaptico, on which this rewrite for Python 3 is heavily based on, see: [Dynaptico PamFax (Python2)].


[Airport1]: https://www.airport1.de/
[PamFax]: http://www.pamfax.biz/
[PamFax for Developers]: https://www.pamfax.biz/developers/introduction/
[Dynaptico PamFax documentation (Python2)]: http://packages.python.org/dynaptico-pamfax
[Dynaptico PamFax (Python2)]: https://github.com/dynaptico/pamfaxp
[Python-Packaging]: https://packaging.python.org/tutorials/packaging-projects/
