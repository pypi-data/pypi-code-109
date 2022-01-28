'''
Module used to setup the default GUI logging and messaging system.
The system contains on a python logging based approach with logfile,
console output and GUI output dependent on startup options and
message logLevel.
'''

import sys
import atexit
import logging
import inspect
from numpy import seterr, seterrcall
from io import StringIO
from ..version import __version__ as str_version


# default options used if nothing is set in the configuration
CONSOLE_LEVEL, FILE_LEVEL, GUI_LEVEL = logging.WARNING, logging.DEBUG, logging.INFO

# set log levels according to options
if 'pdb' in list(sys.modules.keys()) or 'pydevd' in list(sys.modules.keys()):
    # if common debugger modules have been loaded, assume a debug run
    CONSOLE_LEVEL, FILE_LEVEL, GUI_LEVEL = logging.INFO, logging.DEBUG, logging.INFO
elif '--debug' in sys.argv:
    CONSOLE_LEVEL, FILE_LEVEL, GUI_LEVEL = logging.DEBUG, logging.DEBUG, logging.INFO


def genx_exit_message():
    logging.info('*** GenX %s Logging ended ***'%str_version)


# noinspection PyUnusedLocal
def iprint(*objects, sep=None, end=None, file=None, flush=False):
    """
    A logging function that behaves like print but uses logging.info.
    """
    if sep is None:
        sep = ' '
    if end is None:
        end = ''  # '\n'
    logging.info(sep.join(map(str, objects))+end)


class NumpyLogger(logging.getLoggerClass()):
    '''
      A logger that makes sure the actual function definition filename, lineno and function name
      is used for logging numpy floating point errors, not the numpy_logger function.
    '''

    def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None):
        try:
            curframe = inspect.currentframe()
            calframes = inspect.getouterframes(curframe, 2)
            # stack starts with:
            # (this method, debug call, debug call root logger, numpy_logger, actual function, ...)
            ignore, fname, lineno, func, ignore, ignore = calframes[4]
        except Exception:
            fname = 'unknown'
            lineno = -1
            func = 'unknown'
        return logging.getLoggerClass().makeRecord(self, name, level, fname, lineno,
                                                   msg, args, exc_info, func=func, extra=extra)


nplogger = None


def numpy_logger(err, _flag):
    nplogger.debug('numpy floating point error encountered (%s)'%err)


def numpy_set_options():
    seterr(divide='call', over='call', under='ignore', invalid='call')
    seterrcall(numpy_logger)


def setup_system():
    logger = logging.getLogger()
    logger.setLevel(min(CONSOLE_LEVEL, GUI_LEVEL))

    # no console logger for windows (win32gui)
    console = logging.StreamHandler(sys.__stdout__)
    formatter = logging.Formatter('%(levelname) 7s: %(message)s')
    console.setFormatter(formatter)
    console.setLevel(CONSOLE_LEVEL)
    logger.addHandler(console)

    logging.getLogger('matplotlib').setLevel(logging.WARNING)
    if min(CONSOLE_LEVEL, GUI_LEVEL)>logging.DEBUG:
        logging.getLogger('numba').setLevel(logging.WARNING)
    logging.info(f'*** GenX {str_version} Logging started ***')

    # define numpy warning behavior
    global nplogger
    old_class = logging.getLoggerClass()
    logging.setLoggerClass(NumpyLogger)
    nplogger = logging.getLogger('numpy')
    nplogger.setLevel(logging.DEBUG)
    null_handler = logging.StreamHandler(StringIO())
    null_handler.setLevel(logging.CRITICAL)
    nplogger.addHandler(null_handler)
    logging.setLoggerClass(old_class)
    logging.captureWarnings(True)
    numpy_set_options()

    # write information on program exit
    atexit.register(genx_exit_message)


def activate_logging(logfile):
    logger = logging.getLogger()
    logfile = logging.FileHandler(logfile, 'w', encoding='utf-8')
    logger.setLevel(min(logger.getEffectiveLevel(), FILE_LEVEL))
    formatter = logging.Formatter('[%(levelname)s] - %(asctime)s - %(process)d:%(threadName)s:%(filename)s:%(lineno)i:%(funcName)s | %(message)s',
                                  '')
    logfile.setFormatter(formatter)
    logfile.setLevel(FILE_LEVEL)
    logger.addHandler(logfile)
    nplogger.addHandler(logfile)
    logger.info('*** GenX %s Logging started to file ***'%str_version)


_prev_excepthook = None


def excepthook_overwrite(*exc_info):
    # making sure all exceptions are displayed on GUI and logged
    # noinspection PyTypeChecker
    logging.critical('uncought python error', exc_info=exc_info)
    # noinspection PyCallingNonCallable
    return _prev_excepthook(*exc_info)


def activate_excepthook():
    logging.debug("replacing sys.excepthook with user function")
    global _prev_excepthook
    _prev_excepthook = sys.excepthook
    sys.excepthook = excepthook_overwrite
