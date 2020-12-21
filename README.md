# a1pamfax

<img alt="Python versions" src="https://camo.githubusercontent.com/4b34d92404f5a39a6b41ee03b34a2926bbc70db8/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f667269747a636f6e6e656374696f6e2e737667"/> <img src="https://camo.githubusercontent.com/232174f26bac5f71ba94b19698d7374192fbe304/68747470733a2f2f696d672e736869656c64732e696f2f707970692f6c2f667269747a636f6e6e656374696f6e2e737667"/><p/>

[Airport1]'s PamFax - short name **a1pamfax** - is a Python (3.6+) package that implements the [PamFax] API. 

This is an adaption of [Dynaptico PamFax (Python2)] - once written for Python 2 - now adapted to work for Python 3.6 or later.
The old code (and style) has been kept whenever possible, on purpose. The behavior should be nearly the same.

For more information about the PamFax API, visit: [PamFax for Developers].

As this package is still in development, please report any bugs or issues by raising an issue in this [Github] repository.

This module is written for Python 3.6+ and has only been tested against Python 3.9.
There is a big chance it works for previous versions, however, too.

### Installation

You can install ```a1pamfax``` either via the Python Package Index (PyPI) or from source.

To install the latest version via pip:

```
pip install a1pamfax --upgrade
```

This is my first public package following the instructions on [Python-Packaging]. 
So far I included the test, test data (the former pdf file by dynaptico), a config example and a sample. 

### Requirements

It is required to install at least (e.g. via ```pip install requests```):

* requests

### Tests

It is strongly recommended to use the sandbox environment ('sandbox-apifrontend') for testing.
First copy the file ```config.example.py``` and rename it to ```config.py``` and fill in your credentials. Then
run either the sample by:

```
python sample.py
```

or the test suite by:

```
cd test
python test.py
```
        
You may adapt the main method of ```test.py``` to en-/disable the tests you (dis)like.

Depending on the tests you run it might be required that you already received or sent something, e.g. in the
sandbox environment. 
The online storage tests will partially be skipped if you did not authenticate for e.g. Dropbox before, this
is intentionally.

### Usage

There is also a ```sample.py``` provided, but in short: after logging in follow the
[PamFax Processors Documentation]. E.g. Common::GetCurrentSettings is available as
pamfax.get_current_settings() etc. Full example:

```
from config import HOST, USERNAME, PASSWORD, APIKEY, APISECRET
from pamfax import PamFax

pamfax = PamFax(USERNAME, PASSWORD, host=HOST, apikey=APIKEY, apisecret=APISECRET)
response = pamfax.get_current_settings()
print(response)
```

### Documentation

There is no documentation for this package in Python 3 yet. But:
the documentation for the older Python 2 implementation by dynaptico might be still available here:
[Dynaptico PamFax documentation (Python2)]
    
and nearly all methods and signatures have been kept ON PURPOSE, 
just adapted for Python 3. Only few private methods were changed.

See also section Particularities.

### Integrity

All methods in the PamFax API should be implemented by this package, except the ones introduced after Dynaptico
released his Python 2 version. Missing methods will be added, step by step.

Since v0.0.6 Dropbox methods are re-enabled and tested, plus missing methods for Common have been added.

### Particularities

As said, the code is heavily based on an old package for Python 2. It was just adapted to run "the same" on Python 3.
Intentionally nearly all methods and signatures have been kept, except the implementation might be different sometimes.
So the code has only been touched where it was required, e.g. it's using now ```requests```'s session with a timeout
of 30 seconds.
I tried to stick to the coding style of dynaptico.
However, few private methods had to be changed in their signature:

* _get_and_check_response
* _get
* _post   

### Thanks

To Dynaptico, on which this rewrite for Python 3 is heavily based on, see: [Dynaptico PamFax (Python2)].

### Packaging for Python - a small tutorial

For developing ensure the package is uninstalled e.g. in the venv and in test.py set ```develop_mode = True```:
```
pip uninstall a1pamfax
```

Pre-testing: in test.py set ```develop_mode = False```, then for e.g. in the venv do this:
```
python setup.py install
python test.py
```


In general check out [Python-Packaging]. After setting up the Test-PyPI and PyPI accounts continue here.

```
cd \workspace\python\a1pamfax
rd /s /q dist build a1pamfax.egg-info
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
python -m pip install --user --upgrade twine
```

Uploading to testpypi:
```
python -m twine upload --repository testpypi dist/*
```

And after testing, for production use (e.g. in the venv):
```
python -m twine upload dist/*
pip uninstall a1pamfax
pip install a1pamfax --upgrade
```

[Airport1]: https://www.airport1.de/
[PamFax]: http://www.pamfax.biz/
[PamFax for Developers]: https://www.pamfax.biz/developers/introduction/
[PamFax Processors Documentation]: https://sandbox-apifrontend.pamfax.biz/processors/
[Dynaptico PamFax documentation (Python2)]: http://packages.python.org/dynaptico-pamfax
[Dynaptico PamFax (Python2)]: https://github.com/dynaptico/pamfaxp
[Python-Packaging]: https://packaging.python.org/tutorials/packaging-projects/
[Github]: https://github.com/bufemc/a1pamfax
