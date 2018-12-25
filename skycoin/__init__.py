
__version__ = "0.25.0"
init_error = None

try:
    from .skycoin import *
    from .skyerror import *
except (AttributeError, ImportError) as _err :
    init_error = _err

    import sys, traceback
    print("Error initializing skycoin package. Details:", file=sys.stderr)
    exc_info = sys.exc_info()
    traceback.print_exception(*exc_info)
    print("\n\nInport succeeded but package load failed", file=sys.stderr)

