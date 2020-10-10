NAME

    a1pamfax - A Python module that implements the PamFax API.

    For more information about the PamFax API that is used with this module, 
    please see:

        http://www.pamfax.biz/en/extensions/developers/

    As this python module is still in development, please report any bugs or 
    issues by raising an issue here:

        http://github.com/bufemc/a1pamfax/issues

NOTE ON PYTHON VERSIONS

    This module is for python 3.6+ and has only been tested against python 3.6+.

INSTALLATION

    The module is available from packages.python.org and can be installed using:

	    pip install a1pamfax

TESTS

    Run the test suite with the following commands:

        cd test
        python test.py

LOGGING

    This module uses the built-in Python logging.

DOCUMENTATION

    The documentation for the older Python 2 implementation by dynaptico is available at the following location:

        http://packages.python.org/dynaptico-pamfax

    And nearly all methods and signatures have been kept, just adapted for Python 3. Only few private methods changed.

THANKS TO

    Dynaptico, on which this rewrite for Python 3 is heavily based on:

        https://github.com/dynaptico/pamfaxp
